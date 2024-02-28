from finazon_grpc_python.time_series_service import TimeSeriesService, GetTimeSeriesRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError


service = TimeSeriesService('your_api_key')

try:
    request = GetTimeSeriesRequest(ticker='AAPL', dataset='sip_non_pro', interval='1h')
    response = service.get_time_series(request)
    print('Last 1h candle for AAPL:\n')
    print(response.result[0])
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')
