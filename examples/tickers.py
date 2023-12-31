import logging
import grpc
from finazon_grpc_python.tickers_pb2_grpc import TickersServiceStub
from finazon_grpc_python.tickers_pb2 import FindTickersCryptoRequest, FindTickerCryptoResponse


api_url = 'grpc-latest.finazon.io:443'
api_token = 'your_api_key'

# Setup gRPC credentials
call_credentials = grpc.access_token_call_credentials(api_token)
channel_credentials = grpc.ssl_channel_credentials()
credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)

try:
    # Open gRPC channel and call method
    with grpc.secure_channel(api_url, credentials=credentials) as channel:
        stub = TickersServiceStub(channel)
        response: FindTickerCryptoResponse = stub.FindTickersCrypto(FindTickersCryptoRequest())
        # Iterate over tickers response result
        for item in response.result:
            print(f'Ticker: {item.ticker}, publisher: {item.publisher}')
# Catch gRPC exceptions
except grpc.RpcError as e:
    if e.code() == grpc.StatusCode.UNAUTHENTICATED:
        logging.error('Invalid API key was provided')
    else:
        logging.error(f'gRPC exception: {e}')
