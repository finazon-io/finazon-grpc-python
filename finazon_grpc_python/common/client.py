import typing

import grpc
from grpc._channel import _InactiveRpcError

from finazon_grpc_python.common.settings import FINAZON_GRPC_URL
from finazon_grpc_python.common.errors import FinazonGrpcUnauthorizedError, FinazonGrpcRequestError, \
    FinazonGrpcPermissionDeniedError, FinazonGrpcError


class FinazonGrpcClient:
    def __init__(self, api_token: str, ssl_credentials_opts: typing.Optional[dict] = None):
        self.api_token = api_token
        self.ssl_credentials_opts = ssl_credentials_opts if ssl_credentials_opts else {}
        self.channel: typing.Optional[grpc.Channel] = None

    def get_channel(self) -> grpc.Channel:
        if self.channel is None:
            call_credentials = grpc.access_token_call_credentials(self.api_token)
            channel_credentials = grpc.ssl_channel_credentials(**self.ssl_credentials_opts)
            credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
            self.channel = grpc.secure_channel(FINAZON_GRPC_URL, credentials=credentials)
        return self.channel

    def make_request(self, stub_cls, method: str, request):
        try:
            with self.get_channel() as channel:
                stub = stub_cls(channel)
                return getattr(stub, method)(request)
        except _InactiveRpcError as e:
            error_args = [method, e.code().name]
            error_cls = FinazonGrpcRequestError
            if e.code() == grpc.StatusCode.UNAUTHENTICATED:
                error_cls = FinazonGrpcUnauthorizedError
            if e.code() == grpc.StatusCode.PERMISSION_DENIED:
                error_cls = FinazonGrpcPermissionDeniedError
            raise error_cls(e.details(), *error_args)
        except grpc.RpcError as e:
            raise FinazonGrpcError(e)
