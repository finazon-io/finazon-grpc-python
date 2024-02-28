from finazon_grpc_python.datasets_pb2_grpc import DatasetsServiceStub
from finazon_grpc_python.datasets_pb2 import GetDatasetsRequest, GetDatasetsResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class DatasetsService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_datasets(self, request: GetDatasetsRequest) -> GetDatasetsResponse:
        return self.client.make_request(DatasetsServiceStub, 'GetDatasets', request)
