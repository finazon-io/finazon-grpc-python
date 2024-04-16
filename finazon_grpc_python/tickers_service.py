from finazon_grpc_python.tickers_pb2_grpc import TickersServiceStub
from finazon_grpc_python.tickers_pb2 import FindTickersStocksRequest, FindTickersStocksResponse,  FindTickersCryptoRequest, FindTickersCryptoResponse,  FindTickersForexRequest, FindTickersForexResponse,  FindTickersUSRequest, FindTickersUSResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class TickersService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def find_tickers_stocks(self, request: FindTickersStocksRequest) -> FindTickersStocksResponse:
        return self.client.make_request(TickersServiceStub, 'FindTickersStocks', request)

    def find_tickers_crypto(self, request: FindTickersCryptoRequest) -> FindTickersCryptoResponse:
        return self.client.make_request(TickersServiceStub, 'FindTickersCrypto', request)

    def find_tickers_forex(self, request: FindTickersForexRequest) -> FindTickersForexResponse:
        return self.client.make_request(TickersServiceStub, 'FindTickersForex', request)

    def find_tickers_us(self, request: FindTickersUSRequest) -> FindTickersUSResponse:
        return self.client.make_request(TickersServiceStub, 'FindTickersUS', request)
