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
class PublisherItem(google.protobuf.message.Message):
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

global___PublisherItem = PublisherItem

@typing_extensions.final
class GetPublishersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    code: builtins.str
    page: builtins.int
    page_size: builtins.int
    def __init__(
        self,
        *,
        code: builtins.str = ...,
        page: builtins.int = ...,
        page_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "page", b"page", "page_size", b"page_size"]) -> None: ...

global___GetPublishersRequest = GetPublishersRequest

@typing_extensions.final
class GetPublishersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PublisherItem]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___PublisherItem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["result", b"result"]) -> None: ...

global___GetPublishersResponse = GetPublishersResponse
