# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: finazon_grpc_python/trade.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x66inazon_grpc_python/trade.proto\x12\x07\x66inazon\"A\n\nTradesItem\x12\x12\n\ntrade_date\x18\x01 \x01(\x03\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x10\n\x08quantity\x18\x03 \x01(\x03\"\xc4\x02\n\x10GetTradesRequest\x12\x11\n\tpublisher\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12\x0b\n\x03mic\x18\x03 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x04 \x01(\t\x12\x0e\n\x06market\x18\x05 \x01(\t\x12\x10\n\x08start_at\x18\x06 \x01(\x03\x12\x0e\n\x06\x65nd_at\x18\x07 \x01(\x03\x12\x0c\n\x04tape\x18\x08 \x01(\t\x12\x0c\n\x04page\x18\t \x01(\x05\x12\x11\n\tpage_size\x18\n \x01(\x05\x12\r\n\x05order\x18\x0b \x01(\t\x12\x0b\n\x03\x63qs\x18\x0c \x01(\t\x12\x0b\n\x03\x63ik\x18\r \x01(\t\x12\r\n\x05\x63usip\x18\x0e \x01(\t\x12\x0c\n\x04isin\x18\x0f \x01(\t\x12\x16\n\x0e\x63omposite_figi\x18\x10 \x01(\t\x12\x12\n\nshare_figi\x18\x11 \x01(\t\x12\x0b\n\x03lei\x18\x12 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x13 \x01(\t\"8\n\x11GetTradesResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.finazon.TradesItem2T\n\x0cTradeService\x12\x44\n\tGetTrades\x12\x19.finazon.GetTradesRequest\x1a\x1a.finazon.GetTradesResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'finazon_grpc_python.trade_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRADESITEM']._serialized_start=44
  _globals['_TRADESITEM']._serialized_end=109
  _globals['_GETTRADESREQUEST']._serialized_start=112
  _globals['_GETTRADESREQUEST']._serialized_end=436
  _globals['_GETTRADESRESPONSE']._serialized_start=438
  _globals['_GETTRADESRESPONSE']._serialized_end=494
  _globals['_TRADESERVICE']._serialized_start=496
  _globals['_TRADESERVICE']._serialized_end=580
# @@protoc_insertion_point(module_scope)
