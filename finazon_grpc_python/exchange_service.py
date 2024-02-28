from finazon_grpc_python.exchange_pb2_grpc import ExchangeServiceStub
from finazon_grpc_python.exchange_pb2 import GetMarketsCryptoRequest, GetMarketsCryptoResponse,  GetMarketsStocksRequest, GetMarketsStocksResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class ExchangeService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_markets_crypto(self, request: GetMarketsCryptoRequest) -> GetMarketsCryptoResponse:
        return self.client.make_request(ExchangeServiceStub, 'GetMarketsCrypto', request)

    def get_markets_stocks(self, request: GetMarketsStocksRequest) -> GetMarketsStocksResponse:
        return self.client.make_request(ExchangeServiceStub, 'GetMarketsStocks', request)
