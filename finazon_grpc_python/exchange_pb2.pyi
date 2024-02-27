"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetMarketsCryptoRequest(google.protobuf.message.Message):
    """Crypto"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    page: builtins.int
    page_size: builtins.int
    def __init__(
        self,
        *,
        page: builtins.int = ...,
        page_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page", b"page", "page_size", b"page_size"]) -> None: ...

global___GetMarketsCryptoRequest = GetMarketsCryptoRequest

@typing_extensions.final
class MarketsCryptoResponseItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    code: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        code: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "name", b"name"]) -> None: ...

global___MarketsCryptoResponseItem = MarketsCryptoResponseItem

@typing_extensions.final
class GetMarketsCryptoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MarketsCryptoResponseItem]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___MarketsCryptoResponseItem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["result", b"result"]) -> None: ...

global___GetMarketsCryptoResponse = GetMarketsCryptoResponse

@typing_extensions.final
class GetMarketsStocksRequest(google.protobuf.message.Message):
    """Stocks"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COUNTRY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    country: builtins.str
    name: builtins.str
    code: builtins.str
    page: builtins.int
    page_size: builtins.int
    def __init__(
        self,
        *,
        country: builtins.str = ...,
        name: builtins.str = ...,
        code: builtins.str = ...,
        page: builtins.int = ...,
        page_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "country", b"country", "name", b"name", "page", b"page", "page_size", b"page_size"]) -> None: ...

global___GetMarketsStocksRequest = GetMarketsStocksRequest

@typing_extensions.final
class MarketsStocksResponseItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COUNTRY_FIELD_NUMBER: builtins.int
    MIC_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    country: builtins.str
    mic: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        country: builtins.str = ...,
        mic: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["country", b"country", "mic", b"mic", "name", b"name"]) -> None: ...

global___MarketsStocksResponseItem = MarketsStocksResponseItem

@typing_extensions.final
class GetMarketsStocksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MarketsStocksResponseItem]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___MarketsStocksResponseItem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["result", b"result"]) -> None: ...

global___GetMarketsStocksResponse = GetMarketsStocksResponse
