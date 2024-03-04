from finazon_grpc_python.time_series_service import TimeSeriesService, GetTimeSeriesMaRequest, GetTimeSeriesRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError
from finazon_grpc_python.common.utils import convert_response_to_pandas


service = TimeSeriesService('your_api_key')

try:
    request = GetTimeSeriesMaRequest(
        time_series=GetTimeSeriesRequest(ticker='NVDA', interval='1h', dataset='sip_non_pro', page_size=50)
    )
    response = service.get_time_series_ma(request)
    df = convert_response_to_pandas(response)
    print(df.describe())
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')

