from finazon_grpc_python.tickers_service import TickersService, FindTickersCryptoRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError


service = TickersService('your_api_key')

try:
    response = service.find_tickers_crypto(FindTickersCryptoRequest(page_size=10, publisher='binance'))
    for item in response.result:
        print(f'Ticker: {item.ticker}')
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')
