from finazon_grpc_python.sip_pb2_grpc import SipServiceStub
from finazon_grpc_python.sip_pb2 import GetSipTradesRequest, GetSipTradesResponse,  GetSipMarketCenterRequest, GetSipMarketCenterResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class SipService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_trades(self, request: GetSipTradesRequest) -> GetSipTradesResponse:
        return self.client.make_request(SipServiceStub, 'GetTrades', request)

    def get_market_center(self, request: GetSipMarketCenterRequest) -> GetSipMarketCenterResponse:
        return self.client.make_request(SipServiceStub, 'GetMarketCenter', request)
