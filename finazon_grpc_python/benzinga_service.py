from finazon_grpc_python.benzinga_pb2_grpc import BenzingaServiceStub
from finazon_grpc_python.benzinga_pb2 import GetDividentsCalendarRequest, GetDividentsCalendarResponse,  GetEarningsCalendarRequest, GetEarningsCalendarResponse,  GetNewsRequest, GetNewsResponse,  GetIPORequest, GetIPOResponse
from finazon_grpc_python.common.client import FinazonGrpcClient


class BenzingaService:
    def __init__(self, api_token: str):
        self.client = FinazonGrpcClient(api_token)

    def get_dividents_calendar(self, request: GetDividentsCalendarRequest) -> GetDividentsCalendarResponse:
        return self.client.make_request(BenzingaServiceStub, 'GetDividentsCalendar', request)

    def get_earnings_calendar(self, request: GetEarningsCalendarRequest) -> GetEarningsCalendarResponse:
        return self.client.make_request(BenzingaServiceStub, 'GetEarningsCalendar', request)

    def get_news(self, request: GetNewsRequest) -> GetNewsResponse:
        return self.client.make_request(BenzingaServiceStub, 'GetNews', request)

    def get_ipo(self, request: GetIPORequest) -> GetIPOResponse:
        return self.client.make_request(BenzingaServiceStub, 'GetIPO', request)
