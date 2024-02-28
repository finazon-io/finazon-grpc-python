from finazon_grpc_python.forex_pb2_grpc import ForexServiceStub
from finazon_grpc_python.forex_pb2 import GetForexTimeSeriesRequest, GetForexTimeSeriesResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class ForexService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_time_series(self, request: GetForexTimeSeriesRequest) -> GetForexTimeSeriesResponse:
        return self.client.make_request(ForexServiceStub, 'GetTimeSeries', request)
