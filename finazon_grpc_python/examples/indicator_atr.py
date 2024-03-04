from finazon_grpc_python.time_series_service import TimeSeriesService, GetTimeSeriesAtrRequest, GetTimeSeriesRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError


service = TimeSeriesService('your_api_key')

try:
    request = GetTimeSeriesAtrRequest(
        time_series=GetTimeSeriesRequest(ticker='AAPL', interval='1h', dataset='sip_non_pro', page_size=5),
        time_period=16,
    )
    response = service.get_time_series_atr(request)
    print(F'Last ATR value {response.result[0].atr}')
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')

