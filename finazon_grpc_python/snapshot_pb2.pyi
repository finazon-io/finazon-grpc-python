"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetSnapshotRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUBLISHER_FIELD_NUMBER: builtins.int
    TICKER_FIELD_NUMBER: builtins.int
    MARKET_FIELD_NUMBER: builtins.int
    MIC_FIELD_NUMBER: builtins.int
    COUNTRY_FIELD_NUMBER: builtins.int
    CQS_FIELD_NUMBER: builtins.int
    CIK_FIELD_NUMBER: builtins.int
    CUSIP_FIELD_NUMBER: builtins.int
    ISIN_FIELD_NUMBER: builtins.int
    COMPOSITE_FIGI_FIELD_NUMBER: builtins.int
    SHARE_FIGI_FIELD_NUMBER: builtins.int
    LEI_FIELD_NUMBER: builtins.int
    DATASET_FIELD_NUMBER: builtins.int
    publisher: builtins.str
    ticker: builtins.str
    market: builtins.str
    mic: builtins.str
    country: builtins.str
    cqs: builtins.str
    cik: builtins.str
    cusip: builtins.str
    isin: builtins.str
    composite_figi: builtins.str
    share_figi: builtins.str
    lei: builtins.str
    dataset: builtins.str
    def __init__(
        self,
        *,
        publisher: builtins.str = ...,
        ticker: builtins.str = ...,
        market: builtins.str = ...,
        mic: builtins.str = ...,
        country: builtins.str = ...,
        cqs: builtins.str = ...,
        cik: builtins.str = ...,
        cusip: builtins.str = ...,
        isin: builtins.str = ...,
        composite_figi: builtins.str = ...,
        share_figi: builtins.str = ...,
        lei: builtins.str = ...,
        dataset: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cik", b"cik", "composite_figi", b"composite_figi", "country", b"country", "cqs", b"cqs", "cusip", b"cusip", "dataset", b"dataset", "isin", b"isin", "lei", b"lei", "market", b"market", "mic", b"mic", "publisher", b"publisher", "share_figi", b"share_figi", "ticker", b"ticker"]) -> None: ...

global___GetSnapshotRequest = GetSnapshotRequest

@typing_extensions.final
class SnapshotOhlcv(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPEN_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    LOW_FIELD_NUMBER: builtins.int
    CLOSE_FIELD_NUMBER: builtins.int
    VOLUME_FIELD_NUMBER: builtins.int
    open: builtins.float
    high: builtins.float
    low: builtins.float
    close: builtins.float
    volume: builtins.float
    def __init__(
        self,
        *,
        open: builtins.float = ...,
        high: builtins.float = ...,
        low: builtins.float = ...,
        close: builtins.float = ...,
        volume: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["close", b"close", "high", b"high", "low", b"low", "open", b"open", "volume", b"volume"]) -> None: ...

global___SnapshotOhlcv = SnapshotOhlcv

@typing_extensions.final
class SnapshotLastTrade(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EVENT_AT_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    SHARES_FIELD_NUMBER: builtins.int
    event_at: builtins.int
    price: builtins.float
    shares: builtins.int
    def __init__(
        self,
        *,
        event_at: builtins.int = ...,
        price: builtins.float = ...,
        shares: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["event_at", b"event_at", "price", b"price", "shares", b"shares"]) -> None: ...

global___SnapshotLastTrade = SnapshotLastTrade

@typing_extensions.final
class SnapshotLastFiftyTwoWeek(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HIGH_FIELD_NUMBER: builtins.int
    HIGH_AT_FIELD_NUMBER: builtins.int
    LOW_FIELD_NUMBER: builtins.int
    LOW_AT_FIELD_NUMBER: builtins.int
    CHANGE_FIELD_NUMBER: builtins.int
    CHANGE_PERCENT_FIELD_NUMBER: builtins.int
    AVERAGE_VOLUME_FIELD_NUMBER: builtins.int
    high: builtins.float
    high_at: builtins.int
    low: builtins.float
    low_at: builtins.int
    change: builtins.float
    change_percent: builtins.float
    average_volume: builtins.int
    def __init__(
        self,
        *,
        high: builtins.float = ...,
        high_at: builtins.int = ...,
        low: builtins.float = ...,
        low_at: builtins.int = ...,
        change: builtins.float = ...,
        change_percent: builtins.float = ...,
        average_volume: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["average_volume", b"average_volume", "change", b"change", "change_percent", b"change_percent", "high", b"high", "high_at", b"high_at", "low", b"low", "low_at", b"low_at"]) -> None: ...

global___SnapshotLastFiftyTwoWeek = SnapshotLastFiftyTwoWeek

@typing_extensions.final
class SnapshotChange(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DAY_CHANGE_PERCENT_FIELD_NUMBER: builtins.int
    WEEK_CHANGE_PERCENT_FIELD_NUMBER: builtins.int
    MONTH_CHANGE_PERCENT_FIELD_NUMBER: builtins.int
    day_change_percent: builtins.float
    week_change_percent: builtins.float
    month_change_percent: builtins.float
    def __init__(
        self,
        *,
        day_change_percent: builtins.float = ...,
        week_change_percent: builtins.float = ...,
        month_change_percent: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["day_change_percent", b"day_change_percent", "month_change_percent", b"month_change_percent", "week_change_percent", b"week_change_percent"]) -> None: ...

global___SnapshotChange = SnapshotChange

@typing_extensions.final
class GetSnapshotResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LAST_DAY_FIELD_NUMBER: builtins.int
    LAST_MONTH_FIELD_NUMBER: builtins.int
    LAST_TRADE_FIELD_NUMBER: builtins.int
    PREVIOUS_DAY_FIELD_NUMBER: builtins.int
    LAST_FIFTY_TWO_WEEK_FIELD_NUMBER: builtins.int
    CHANGE_FIELD_NUMBER: builtins.int
    @property
    def last_day(self) -> global___SnapshotOhlcv: ...
    @property
    def last_month(self) -> global___SnapshotOhlcv: ...
    @property
    def last_trade(self) -> global___SnapshotLastTrade: ...
    @property
    def previous_day(self) -> global___SnapshotOhlcv: ...
    @property
    def last_fifty_two_week(self) -> global___SnapshotLastFiftyTwoWeek: ...
    @property
    def change(self) -> global___SnapshotChange: ...
    def __init__(
        self,
        *,
        last_day: global___SnapshotOhlcv | None = ...,
        last_month: global___SnapshotOhlcv | None = ...,
        last_trade: global___SnapshotLastTrade | None = ...,
        previous_day: global___SnapshotOhlcv | None = ...,
        last_fifty_two_week: global___SnapshotLastFiftyTwoWeek | None = ...,
        change: global___SnapshotChange | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["change", b"change", "last_day", b"last_day", "last_fifty_two_week", b"last_fifty_two_week", "last_month", b"last_month", "last_trade", b"last_trade", "previous_day", b"previous_day"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["change", b"change", "last_day", b"last_day", "last_fifty_two_week", b"last_fifty_two_week", "last_month", b"last_month", "last_trade", b"last_trade", "previous_day", b"previous_day"]) -> None: ...

global___GetSnapshotResponse = GetSnapshotResponse
