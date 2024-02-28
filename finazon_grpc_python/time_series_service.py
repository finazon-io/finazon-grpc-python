from finazon_grpc_python.time_series_pb2_grpc import TimeSeriesServiceStub
from finazon_grpc_python.time_series_pb2 import GetTimeSeriesRequest, GetTimeSeriesResponse,  GetTimeSeriesAtrRequest, GetTimeSeriesAtrResponse,  GetTimeSeriesBBandsRequest, GetTimeSeriesBBandsResponse,  GetTimeSeriesIchimokuRequest, GetTimeSeriesIchimokuResponse,  GetTimeSeriesMaRequest, GetTimeSeriesMaResponse,  GetTimeSeriesMacdRequest, GetTimeSeriesMacdResponse,  GetTimeSeriesObvRequest, GetTimeSeriesObvResponse,  GetTimeSeriesRsiRequest, GetTimeSeriesRsiResponse,  GetTimeSeriesSarRequest, GetTimeSeriesSarResponse,  GetTimeSeriesStochRequest, GetTimeSeriesStochResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class TimeSeriesService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_time_series(self, request: GetTimeSeriesRequest) -> GetTimeSeriesResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeries', request)

    def get_time_series_atr(self, request: GetTimeSeriesAtrRequest) -> GetTimeSeriesAtrResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeriesAtr', request)

    def get_time_series_b_bands(self, request: GetTimeSeriesBBandsRequest) -> GetTimeSeriesBBandsResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeriesBBands', request)

    def get_time_series_ichimoku(self, request: GetTimeSeriesIchimokuRequest) -> GetTimeSeriesIchimokuResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeriesIchimoku', request)

    def get_time_series_ma(self, request: GetTimeSeriesMaRequest) -> GetTimeSeriesMaResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeriesMa', request)

    def get_time_series_macd(self, request: GetTimeSeriesMacdRequest) -> GetTimeSeriesMacdResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeriesMacd', request)

    def get_time_series_obv(self, request: GetTimeSeriesObvRequest) -> GetTimeSeriesObvResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeriesObv', request)

    def get_time_series_rsi(self, request: GetTimeSeriesRsiRequest) -> GetTimeSeriesRsiResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeriesRsi', request)

    def get_time_series_sar(self, request: GetTimeSeriesSarRequest) -> GetTimeSeriesSarResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeriesSar', request)

    def get_time_series_stoch(self, request: GetTimeSeriesStochRequest) -> GetTimeSeriesStochResponse:
        return self.client.make_request(TimeSeriesServiceStub, 'GetTimeSeriesStoch', request)
