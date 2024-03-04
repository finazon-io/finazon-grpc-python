from finazon_grpc_python.time_series_service import TimeSeriesService, GetTimeSeriesMaRequest, GetTimeSeriesRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError


service = TimeSeriesService('your_api_key')

try:
    request = GetTimeSeriesMaRequest(
        time_series=GetTimeSeriesRequest(ticker='AAPL', interval='1h', dataset='sip_non_pro', page_size=10),
        time_period=100,
    )
    response = service.get_time_series_ma(request)
    print(response.result)
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')
