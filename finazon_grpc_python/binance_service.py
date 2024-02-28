from finazon_grpc_python.binance_pb2_grpc import BinanceServiceStub
from finazon_grpc_python.binance_pb2 import GetBinanceTimeSeriesRequest, GetBinanceTimeSeriesResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class BinanceService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_time_series(self, request: GetBinanceTimeSeriesRequest) -> GetBinanceTimeSeriesResponse:
        return self.client.make_request(BinanceServiceStub, 'GetTimeSeries', request)
