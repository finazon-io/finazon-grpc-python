from finazon_grpc_python.time_series_service import TimeSeriesService, GetTimeSeriesRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError
from finazon_grpc_python.common.utils import convert_response_to_pandas


service = TimeSeriesService('your_api_key')

try:
    request = GetTimeSeriesRequest(ticker='AAPL', dataset='us_stocks_essential', interval='1h', page_size=50)
    response = service.get_time_series(request)
    df = convert_response_to_pandas(response)
    print(df.describe())
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')
