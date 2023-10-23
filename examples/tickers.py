import grpc
from finazon_grpc_python.tickers_pb2_grpc import TickersServiceStub
from finazon_grpc_python.tickers_pb2 import FindTickersCryptoRequest, FindTickerCryptoResponse


api_url = 'grpc-latest.finazon.io:443'
api_token = 'type_your_api_key_here'


def get_credentials():
    call_credentials = grpc.access_token_call_credentials(api_token)
    channel_credentials = grpc.ssl_channel_credentials()
    return grpc.composite_channel_credentials(channel_credentials, call_credentials)


def get_tickers_crypto() -> FindTickerCryptoResponse:
    credentials = get_credentials()
    with grpc.secure_channel(api_url, credentials=credentials) as channel:
        stub = TickersServiceStub(channel)
        response = stub.FindTickersCrypto(FindTickersCryptoRequest())
        return response


if __name__ == '__main__':
    try:
        r = get_tickers_crypto()
        print(r)
    except grpc.RpcError as e:
        print(f'Error response: {e}')
