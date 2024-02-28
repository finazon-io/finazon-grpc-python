from finazon_grpc_python.trade_pb2_grpc import TradeServiceStub
from finazon_grpc_python.trade_pb2 import GetTradesRequest, GetTradesResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class TradeService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_trades(self, request: GetTradesRequest) -> GetTradesResponse:
        return self.client.make_request(TradeServiceStub, 'GetTrades', request)
