from finazon_grpc_python.api_usage_pb2_grpc import ApiUsageServiceStub
from finazon_grpc_python.api_usage_pb2 import GetApiUsageRequest, GetApiUsageResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class ApiUsageService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_api_usage(self, request: GetApiUsageRequest) -> GetApiUsageResponse:
        return self.client.make_request(ApiUsageServiceStub, 'GetApiUsage', request)
