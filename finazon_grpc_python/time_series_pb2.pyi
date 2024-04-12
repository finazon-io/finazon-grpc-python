"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TimeSeries(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    OPEN_FIELD_NUMBER: builtins.int
    CLOSE_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    LOW_FIELD_NUMBER: builtins.int
    VOLUME_FIELD_NUMBER: builtins.int
    timestamp: builtins.int
    open: builtins.float
    close: builtins.float
    high: builtins.float
    low: builtins.float
    volume: builtins.float
    def __init__(
        self,
        *,
        timestamp: builtins.int = ...,
        open: builtins.float = ...,
        close: builtins.float = ...,
        high: builtins.float = ...,
        low: builtins.float = ...,
        volume: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["close", b"close", "high", b"high", "low", b"low", "open", b"open", "timestamp", b"timestamp", "volume", b"volume"]) -> None: ...

global___TimeSeries = TimeSeries

@typing.final
class GetTimeSeriesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUBLISHER_FIELD_NUMBER: builtins.int
    TICKER_FIELD_NUMBER: builtins.int
    EXCHANGE_FIELD_NUMBER: builtins.int
    MIC_FIELD_NUMBER: builtins.int
    COUNTRY_FIELD_NUMBER: builtins.int
    INSTRUMENT_TYPE_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    START_AT_FIELD_NUMBER: builtins.int
    END_AT_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    PREPOST_FIELD_NUMBER: builtins.int
    MARKET_FIELD_NUMBER: builtins.int
    DATASET_FIELD_NUMBER: builtins.int
    CQS_FIELD_NUMBER: builtins.int
    CIK_FIELD_NUMBER: builtins.int
    CUSIP_FIELD_NUMBER: builtins.int
    ISIN_FIELD_NUMBER: builtins.int
    COMPOSITE_FIGI_FIELD_NUMBER: builtins.int
    SHARE_FIGI_FIELD_NUMBER: builtins.int
    LEI_FIELD_NUMBER: builtins.int
    ADJUST_FIELD_NUMBER: builtins.int
    publisher: builtins.str
    ticker: builtins.str
    exchange: builtins.str
    mic: builtins.str
    country: builtins.str
    instrument_type: builtins.str
    interval: builtins.str
    start_at: builtins.int
    end_at: builtins.int
    page: builtins.int
    page_size: builtins.int
    order: builtins.str
    prepost: builtins.bool
    market: builtins.str
    dataset: builtins.str
    cqs: builtins.str
    cik: builtins.str
    cusip: builtins.str
    isin: builtins.str
    composite_figi: builtins.str
    share_figi: builtins.str
    lei: builtins.str
    adjust: builtins.str
    def __init__(
        self,
        *,
        publisher: builtins.str = ...,
        ticker: builtins.str = ...,
        exchange: builtins.str = ...,
        mic: builtins.str = ...,
        country: builtins.str = ...,
        instrument_type: builtins.str = ...,
        interval: builtins.str = ...,
        start_at: builtins.int = ...,
        end_at: builtins.int = ...,
        page: builtins.int = ...,
        page_size: builtins.int = ...,
        order: builtins.str = ...,
        prepost: builtins.bool = ...,
        market: builtins.str = ...,
        dataset: builtins.str = ...,
        cqs: builtins.str = ...,
        cik: builtins.str = ...,
        cusip: builtins.str = ...,
        isin: builtins.str = ...,
        composite_figi: builtins.str = ...,
        share_figi: builtins.str = ...,
        lei: builtins.str = ...,
        adjust: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["adjust", b"adjust", "cik", b"cik", "composite_figi", b"composite_figi", "country", b"country", "cqs", b"cqs", "cusip", b"cusip", "dataset", b"dataset", "end_at", b"end_at", "exchange", b"exchange", "instrument_type", b"instrument_type", "interval", b"interval", "isin", b"isin", "lei", b"lei", "market", b"market", "mic", b"mic", "order", b"order", "page", b"page", "page_size", b"page_size", "prepost", b"prepost", "publisher", b"publisher", "share_figi", b"share_figi", "start_at", b"start_at", "ticker", b"ticker"]) -> None: ...

global___GetTimeSeriesRequest = GetTimeSeriesRequest

@typing.final
class GetTimeSeriesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TimeSeries]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___TimeSeries] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesResponse = GetTimeSeriesResponse

@typing.final
class GetTimeSeriesAtrRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_PERIOD_FIELD_NUMBER: builtins.int
    TIME_SERIES_FIELD_NUMBER: builtins.int
    time_period: builtins.int
    @property
    def time_series(self) -> global___GetTimeSeriesRequest: ...
    def __init__(
        self,
        *,
        time_period: builtins.int = ...,
        time_series: global___GetTimeSeriesRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series", b"time_series"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["time_period", b"time_period", "time_series", b"time_series"]) -> None: ...

global___GetTimeSeriesAtrRequest = GetTimeSeriesAtrRequest

@typing.final
class GetTimeSeriesAtrResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Atr(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        ATR_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        atr: builtins.str
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            atr: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["atr", b"atr", "timestamp", b"timestamp"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetTimeSeriesAtrResponse.Atr]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetTimeSeriesAtrResponse.Atr] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesAtrResponse = GetTimeSeriesAtrResponse

@typing.final
class GetTimeSeriesBBandsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_PERIOD_FIELD_NUMBER: builtins.int
    SERIES_TYPE_FIELD_NUMBER: builtins.int
    SD_FIELD_NUMBER: builtins.int
    MA_TYPE_FIELD_NUMBER: builtins.int
    TIME_SERIES_FIELD_NUMBER: builtins.int
    time_period: builtins.int
    series_type: builtins.str
    sd: builtins.float
    ma_type: builtins.str
    @property
    def time_series(self) -> global___GetTimeSeriesRequest: ...
    def __init__(
        self,
        *,
        time_period: builtins.int = ...,
        series_type: builtins.str = ...,
        sd: builtins.float = ...,
        ma_type: builtins.str = ...,
        time_series: global___GetTimeSeriesRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series", b"time_series"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ma_type", b"ma_type", "sd", b"sd", "series_type", b"series_type", "time_period", b"time_period", "time_series", b"time_series"]) -> None: ...

global___GetTimeSeriesBBandsRequest = GetTimeSeriesBBandsRequest

@typing.final
class GetTimeSeriesBBandsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class BBands(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        UPPER_BAND_FIELD_NUMBER: builtins.int
        MIDDLE_BAND_FIELD_NUMBER: builtins.int
        LOWER_BAND_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        upper_band: builtins.str
        middle_band: builtins.str
        lower_band: builtins.str
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            upper_band: builtins.str = ...,
            middle_band: builtins.str = ...,
            lower_band: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["lower_band", b"lower_band", "middle_band", b"middle_band", "timestamp", b"timestamp", "upper_band", b"upper_band"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetTimeSeriesBBandsResponse.BBands]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetTimeSeriesBBandsResponse.BBands] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesBBandsResponse = GetTimeSeriesBBandsResponse

@typing.final
class GetTimeSeriesIchimokuRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONVERSION_LINE_PERIOD_FIELD_NUMBER: builtins.int
    BASE_LINE_PERIOD_FIELD_NUMBER: builtins.int
    LEADING_SPAN_B_PERIOD_FIELD_NUMBER: builtins.int
    LAGGING_SPAN_PERIOD_FIELD_NUMBER: builtins.int
    INCLUDE_AHEAD_SPAN_PERIOD_FIELD_NUMBER: builtins.int
    TIME_SERIES_FIELD_NUMBER: builtins.int
    conversion_line_period: builtins.int
    base_line_period: builtins.int
    leading_span_b_period: builtins.int
    lagging_span_period: builtins.int
    include_ahead_span_period: builtins.bool
    @property
    def time_series(self) -> global___GetTimeSeriesRequest: ...
    def __init__(
        self,
        *,
        conversion_line_period: builtins.int = ...,
        base_line_period: builtins.int = ...,
        leading_span_b_period: builtins.int = ...,
        lagging_span_period: builtins.int = ...,
        include_ahead_span_period: builtins.bool = ...,
        time_series: global___GetTimeSeriesRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series", b"time_series"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["base_line_period", b"base_line_period", "conversion_line_period", b"conversion_line_period", "include_ahead_span_period", b"include_ahead_span_period", "lagging_span_period", b"lagging_span_period", "leading_span_b_period", b"leading_span_b_period", "time_series", b"time_series"]) -> None: ...

global___GetTimeSeriesIchimokuRequest = GetTimeSeriesIchimokuRequest

@typing.final
class GetTimeSeriesIchimokuResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Ichimoku(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        TENKAN_SEN_FIELD_NUMBER: builtins.int
        KIJUN_SEN_FIELD_NUMBER: builtins.int
        SENKOU_SPAN_A_FIELD_NUMBER: builtins.int
        SENKOU_SPAN_B_FIELD_NUMBER: builtins.int
        CHIKOU_SPAN_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        tenkan_sen: builtins.str
        kijun_sen: builtins.str
        senkou_span_a: builtins.str
        senkou_span_b: builtins.str
        chikou_span: builtins.str
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            tenkan_sen: builtins.str = ...,
            kijun_sen: builtins.str = ...,
            senkou_span_a: builtins.str = ...,
            senkou_span_b: builtins.str = ...,
            chikou_span: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["chikou_span", b"chikou_span", "kijun_sen", b"kijun_sen", "senkou_span_a", b"senkou_span_a", "senkou_span_b", b"senkou_span_b", "tenkan_sen", b"tenkan_sen", "timestamp", b"timestamp"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetTimeSeriesIchimokuResponse.Ichimoku]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetTimeSeriesIchimokuResponse.Ichimoku] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesIchimokuResponse = GetTimeSeriesIchimokuResponse

@typing.final
class GetTimeSeriesMaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_PERIOD_FIELD_NUMBER: builtins.int
    SERIES_TYPE_FIELD_NUMBER: builtins.int
    MA_TYPE_FIELD_NUMBER: builtins.int
    TIME_SERIES_FIELD_NUMBER: builtins.int
    time_period: builtins.int
    series_type: builtins.str
    ma_type: builtins.str
    @property
    def time_series(self) -> global___GetTimeSeriesRequest: ...
    def __init__(
        self,
        *,
        time_period: builtins.int = ...,
        series_type: builtins.str = ...,
        ma_type: builtins.str = ...,
        time_series: global___GetTimeSeriesRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series", b"time_series"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ma_type", b"ma_type", "series_type", b"series_type", "time_period", b"time_period", "time_series", b"time_series"]) -> None: ...

global___GetTimeSeriesMaRequest = GetTimeSeriesMaRequest

@typing.final
class GetTimeSeriesMaResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Ma(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        MA_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        ma: builtins.str
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            ma: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["ma", b"ma", "timestamp", b"timestamp"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetTimeSeriesMaResponse.Ma]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetTimeSeriesMaResponse.Ma] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesMaResponse = GetTimeSeriesMaResponse

@typing.final
class GetTimeSeriesMacdRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIES_TYPE_FIELD_NUMBER: builtins.int
    FAST_PERIOD_FIELD_NUMBER: builtins.int
    SLOW_PERIOD_FIELD_NUMBER: builtins.int
    SIGNAL_PERIOD_FIELD_NUMBER: builtins.int
    TIME_SERIES_FIELD_NUMBER: builtins.int
    series_type: builtins.str
    fast_period: builtins.int
    slow_period: builtins.int
    signal_period: builtins.int
    @property
    def time_series(self) -> global___GetTimeSeriesRequest: ...
    def __init__(
        self,
        *,
        series_type: builtins.str = ...,
        fast_period: builtins.int = ...,
        slow_period: builtins.int = ...,
        signal_period: builtins.int = ...,
        time_series: global___GetTimeSeriesRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series", b"time_series"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["fast_period", b"fast_period", "series_type", b"series_type", "signal_period", b"signal_period", "slow_period", b"slow_period", "time_series", b"time_series"]) -> None: ...

global___GetTimeSeriesMacdRequest = GetTimeSeriesMacdRequest

@typing.final
class GetTimeSeriesMacdResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Macd(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        MACD_FIELD_NUMBER: builtins.int
        MACD_SIGNAL_FIELD_NUMBER: builtins.int
        MACD_HIST_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        macd: builtins.str
        macd_signal: builtins.str
        macd_hist: builtins.str
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            macd: builtins.str = ...,
            macd_signal: builtins.str = ...,
            macd_hist: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["macd", b"macd", "macd_hist", b"macd_hist", "macd_signal", b"macd_signal", "timestamp", b"timestamp"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetTimeSeriesMacdResponse.Macd]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetTimeSeriesMacdResponse.Macd] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesMacdResponse = GetTimeSeriesMacdResponse

@typing.final
class GetTimeSeriesObvRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIES_TYPE_FIELD_NUMBER: builtins.int
    TIME_SERIES_FIELD_NUMBER: builtins.int
    series_type: builtins.str
    @property
    def time_series(self) -> global___GetTimeSeriesRequest: ...
    def __init__(
        self,
        *,
        series_type: builtins.str = ...,
        time_series: global___GetTimeSeriesRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series", b"time_series"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["series_type", b"series_type", "time_series", b"time_series"]) -> None: ...

global___GetTimeSeriesObvRequest = GetTimeSeriesObvRequest

@typing.final
class GetTimeSeriesObvResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Obv(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        OBV_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        obv: builtins.str
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            obv: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["obv", b"obv", "timestamp", b"timestamp"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetTimeSeriesObvResponse.Obv]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetTimeSeriesObvResponse.Obv] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesObvResponse = GetTimeSeriesObvResponse

@typing.final
class GetTimeSeriesRsiRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_PERIOD_FIELD_NUMBER: builtins.int
    SERIES_TYPE_FIELD_NUMBER: builtins.int
    TIME_SERIES_FIELD_NUMBER: builtins.int
    time_period: builtins.int
    series_type: builtins.str
    @property
    def time_series(self) -> global___GetTimeSeriesRequest: ...
    def __init__(
        self,
        *,
        time_period: builtins.int = ...,
        series_type: builtins.str = ...,
        time_series: global___GetTimeSeriesRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series", b"time_series"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["series_type", b"series_type", "time_period", b"time_period", "time_series", b"time_series"]) -> None: ...

global___GetTimeSeriesRsiRequest = GetTimeSeriesRsiRequest

@typing.final
class GetTimeSeriesRsiResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Rsi(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        RSI_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        rsi: builtins.str
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            rsi: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["rsi", b"rsi", "timestamp", b"timestamp"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetTimeSeriesRsiResponse.Rsi]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetTimeSeriesRsiResponse.Rsi] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesRsiResponse = GetTimeSeriesRsiResponse

@typing.final
class GetTimeSeriesSarRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCELERATION_FIELD_NUMBER: builtins.int
    MAXIMUM_FIELD_NUMBER: builtins.int
    TIME_SERIES_FIELD_NUMBER: builtins.int
    acceleration: builtins.float
    maximum: builtins.float
    @property
    def time_series(self) -> global___GetTimeSeriesRequest: ...
    def __init__(
        self,
        *,
        acceleration: builtins.float = ...,
        maximum: builtins.float = ...,
        time_series: global___GetTimeSeriesRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series", b"time_series"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["acceleration", b"acceleration", "maximum", b"maximum", "time_series", b"time_series"]) -> None: ...

global___GetTimeSeriesSarRequest = GetTimeSeriesSarRequest

@typing.final
class GetTimeSeriesSarResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Sar(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        SAR_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        sar: builtins.str
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            sar: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["sar", b"sar", "timestamp", b"timestamp"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetTimeSeriesSarResponse.Sar]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetTimeSeriesSarResponse.Sar] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesSarResponse = GetTimeSeriesSarResponse

@typing.final
class GetTimeSeriesStochRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FAST_K_PERIOD_FIELD_NUMBER: builtins.int
    SLOW_K_PERIOD_FIELD_NUMBER: builtins.int
    SLOW_D_PERIOD_FIELD_NUMBER: builtins.int
    SLOW_KMA_TYPE_FIELD_NUMBER: builtins.int
    SLOW_DMA_TYPE_FIELD_NUMBER: builtins.int
    TIME_SERIES_FIELD_NUMBER: builtins.int
    fast_k_period: builtins.int
    slow_k_period: builtins.int
    slow_d_period: builtins.int
    slow_kma_type: builtins.str
    slow_dma_type: builtins.str
    @property
    def time_series(self) -> global___GetTimeSeriesRequest: ...
    def __init__(
        self,
        *,
        fast_k_period: builtins.int = ...,
        slow_k_period: builtins.int = ...,
        slow_d_period: builtins.int = ...,
        slow_kma_type: builtins.str = ...,
        slow_dma_type: builtins.str = ...,
        time_series: global___GetTimeSeriesRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series", b"time_series"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["fast_k_period", b"fast_k_period", "slow_d_period", b"slow_d_period", "slow_dma_type", b"slow_dma_type", "slow_k_period", b"slow_k_period", "slow_kma_type", b"slow_kma_type", "time_series", b"time_series"]) -> None: ...

global___GetTimeSeriesStochRequest = GetTimeSeriesStochRequest

@typing.final
class GetTimeSeriesStochResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Stoch(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        SLOW_K_FIELD_NUMBER: builtins.int
        SLOW_D_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        slow_k: builtins.str
        slow_d: builtins.str
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            slow_k: builtins.str = ...,
            slow_d: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["slow_d", b"slow_d", "slow_k", b"slow_k", "timestamp", b"timestamp"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetTimeSeriesStochResponse.Stoch]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetTimeSeriesStochResponse.Stoch] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___GetTimeSeriesStochResponse = GetTimeSeriesStochResponse
