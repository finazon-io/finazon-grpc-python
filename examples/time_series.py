import logging
import grpc
from finazon_grpc_python.time_series_pb2_grpc import TimeSeriesServiceStub
from finazon_grpc_python.time_series_pb2 import GetTimeSeriesRequest, GetTimeSeriesResponse


api_url = 'grpc-latest.finazon.io:443'
api_token = 'your_api_key'

# Setup gRPC credentials
call_credentials = grpc.access_token_call_credentials(api_token)
channel_credentials = grpc.ssl_channel_credentials()
credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)

try:
    # Open gRPC channel and call method
    with grpc.secure_channel(api_url, credentials=credentials) as channel:
        stub = TimeSeriesServiceStub(channel)
        request = GetTimeSeriesRequest(ticker="AAPL", dataset="sip_non_pro")
        response: GetTimeSeriesResponse = stub.GetTimeSeries(request)

        # Iterate over time series response result
        for item in response.result:
            print(item)
# Catch gRPC exceptions
except grpc.RpcError as e:
    if e.code() == grpc.StatusCode.UNAUTHENTICATED:
        logging.error('Invalid API key was provided')
    else:
        logging.error(f'gRPC exception: {e}')
