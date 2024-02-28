from finazon_grpc_python.sec_pb2_grpc import SecServiceStub
from finazon_grpc_python.sec_pb2 import GetSecFillingsRequest, GetSecFillingsResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class SecService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_filings(self, request: GetSecFillingsRequest) -> GetSecFillingsResponse:
        return self.client.make_request(SecServiceStub, 'GetFilings', request)
