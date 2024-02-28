from finazon_grpc_python.snapshot_pb2_grpc import SnapshotServiceStub
from finazon_grpc_python.snapshot_pb2 import GetSnapshotRequest, GetSnapshotResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class SnapshotService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_snapshot(self, request: GetSnapshotRequest) -> GetSnapshotResponse:
        return self.client.make_request(SnapshotServiceStub, 'GetSnapshot', request)
