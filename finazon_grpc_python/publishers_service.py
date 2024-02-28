from finazon_grpc_python.publishers_pb2_grpc import PublisherServiceStub
from finazon_grpc_python.publishers_pb2 import GetPublishersRequest, GetPublishersResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class PublisherService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_publishers(self, request: GetPublishersRequest) -> GetPublishersResponse:
        return self.client.make_request(PublisherServiceStub, 'GetPublishers', request)
