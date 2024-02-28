from finazon_grpc_python.crypto_pb2_grpc import CryptoServiceStub
from finazon_grpc_python.crypto_pb2 import GetCryptoTimeSeriesRequest, GetCryptoTimeSeriesResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class CryptoService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_time_series(self, request: GetCryptoTimeSeriesRequest) -> GetCryptoTimeSeriesResponse:
        return self.client.make_request(CryptoServiceStub, 'GetTimeSeries', request)
