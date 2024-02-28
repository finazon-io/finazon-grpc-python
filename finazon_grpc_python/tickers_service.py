from finazon_grpc_python.tickers_pb2_grpc import TickersServiceStub
from finazon_grpc_python.tickers_pb2 import FindTickersStocksRequest, FindTickerStocksResponse,  FindTickersCryptoRequest, FindTickerCryptoResponse,  FindTickersForexRequest, FindTickerForexResponse,  FindTickerUSRequest, FindTickerUSResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class TickersService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def find_tickers_stocks(self, request: FindTickersStocksRequest) -> FindTickerStocksResponse:
        return self.client.make_request(TickersServiceStub, 'FindTickersStocks', request)

    def find_tickers_crypto(self, request: FindTickersCryptoRequest) -> FindTickerCryptoResponse:
        return self.client.make_request(TickersServiceStub, 'FindTickersCrypto', request)

    def find_tickers_forex(self, request: FindTickersForexRequest) -> FindTickerForexResponse:
        return self.client.make_request(TickersServiceStub, 'FindTickersForex', request)

    def find_ticker_us(self, request: FindTickerUSRequest) -> FindTickerUSResponse:
        return self.client.make_request(TickersServiceStub, 'FindTickerUS', request)
