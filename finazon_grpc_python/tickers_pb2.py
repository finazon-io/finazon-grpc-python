# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: finazon_grpc_python/tickers.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!finazon_grpc_python/tickers.proto\x12\x07\x66inazon\"p\n\x10TickerStocksInfo\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x12\x10\n\x08\x63urrency\x18\x03 \x01(\t\x12\x11\n\tpublisher\x18\x04 \x01(\t\x12\x16\n\x0epublisher_name\x18\x05 \x01(\t\"\xfd\x01\n\x18\x46indTickersStocksRequest\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x11\n\tpublisher\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\x0b\n\x03mic\x18\x04 \x01(\t\x12\x0c\n\x04page\x18\x05 \x01(\x05\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12\x0b\n\x03\x63qs\x18\x0b \x01(\t\x12\x0b\n\x03\x63ik\x18\x0c \x01(\t\x12\r\n\x05\x63usip\x18\r \x01(\t\x12\x0c\n\x04isin\x18\x0e \x01(\t\x12\x16\n\x0e\x63omposite_figi\x18\x0f \x01(\t\x12\x12\n\nshare_figi\x18\x10 \x01(\t\x12\x0b\n\x03lei\x18\x11 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x12 \x01(\t\"F\n\x19\x46indTickersStocksResponse\x12)\n\x06result\x18\x01 \x03(\x0b\x32\x19.finazon.TickerStocksInfo\"M\n\x10TickerCryptoInfo\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x11\n\tpublisher\x18\x02 \x01(\t\x12\x16\n\x0epublisher_name\x18\x03 \x01(\t\"n\n\x18\x46indTickersCryptoRequest\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x11\n\tpublisher\x18\x02 \x01(\t\x12\x0e\n\x06market\x18\x03 \x01(\t\x12\x0c\n\x04page\x18\x04 \x01(\x05\x12\x11\n\tpage_size\x18\x05 \x01(\x05\"F\n\x19\x46indTickersCryptoResponse\x12)\n\x06result\x18\x01 \x03(\x0b\x32\x19.finazon.TickerCryptoInfo\"!\n\x0fTickerForexInfo\x12\x0e\n\x06ticker\x18\x01 \x01(\t\"J\n\x17\x46indTickersForexRequest\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\"D\n\x18\x46indTickersForexResponse\x12(\n\x06result\x18\x01 \x03(\x0b\x32\x18.finazon.TickerForexInfo\"\xa9\x01\n\x0cTickerUSInfo\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x10\n\x08security\x18\x03 \x01(\t\x12\x0b\n\x03mic\x18\x04 \x01(\t\x12\x12\n\nasset_type\x18\x05 \x01(\t\x12\x0b\n\x03\x63ik\x18\x07 \x01(\t\x12\x16\n\x0e\x63omposite_figi\x18\n \x01(\t\x12\x12\n\nshare_figi\x18\x0b \x01(\t\x12\x0b\n\x03lei\x18\x0c \x01(\t\"\xc4\x01\n\x14\x46indTickersUSRequest\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x0b\n\x03mic\x18\x02 \x01(\t\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x0b\n\x03\x63qs\x18\x05 \x01(\t\x12\x0b\n\x03\x63ik\x18\x06 \x01(\t\x12\r\n\x05\x63usip\x18\x07 \x01(\t\x12\x0c\n\x04isin\x18\x08 \x01(\t\x12\x16\n\x0e\x63omposite_figi\x18\t \x01(\t\x12\x12\n\nshare_figi\x18\n \x01(\t\x12\x0b\n\x03lei\x18\x0b \x01(\t\">\n\x15\x46indTickersUSResponse\x12%\n\x06result\x18\x01 \x03(\x0b\x32\x15.finazon.TickerUSInfo2\xf9\x02\n\x0eTickersService\x12\\\n\x11\x46indTickersStocks\x12!.finazon.FindTickersStocksRequest\x1a\".finazon.FindTickersStocksResponse\"\x00\x12\\\n\x11\x46indTickersCrypto\x12!.finazon.FindTickersCryptoRequest\x1a\".finazon.FindTickersCryptoResponse\"\x00\x12Y\n\x10\x46indTickersForex\x12 .finazon.FindTickersForexRequest\x1a!.finazon.FindTickersForexResponse\"\x00\x12P\n\rFindTickersUS\x12\x1d.finazon.FindTickersUSRequest\x1a\x1e.finazon.FindTickersUSResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'finazon_grpc_python.tickers_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TICKERSTOCKSINFO']._serialized_start=46
  _globals['_TICKERSTOCKSINFO']._serialized_end=158
  _globals['_FINDTICKERSSTOCKSREQUEST']._serialized_start=161
  _globals['_FINDTICKERSSTOCKSREQUEST']._serialized_end=414
  _globals['_FINDTICKERSSTOCKSRESPONSE']._serialized_start=416
  _globals['_FINDTICKERSSTOCKSRESPONSE']._serialized_end=486
  _globals['_TICKERCRYPTOINFO']._serialized_start=488
  _globals['_TICKERCRYPTOINFO']._serialized_end=565
  _globals['_FINDTICKERSCRYPTOREQUEST']._serialized_start=567
  _globals['_FINDTICKERSCRYPTOREQUEST']._serialized_end=677
  _globals['_FINDTICKERSCRYPTORESPONSE']._serialized_start=679
  _globals['_FINDTICKERSCRYPTORESPONSE']._serialized_end=749
  _globals['_TICKERFOREXINFO']._serialized_start=751
  _globals['_TICKERFOREXINFO']._serialized_end=784
  _globals['_FINDTICKERSFOREXREQUEST']._serialized_start=786
  _globals['_FINDTICKERSFOREXREQUEST']._serialized_end=860
  _globals['_FINDTICKERSFOREXRESPONSE']._serialized_start=862
  _globals['_FINDTICKERSFOREXRESPONSE']._serialized_end=930
  _globals['_TICKERUSINFO']._serialized_start=933
  _globals['_TICKERUSINFO']._serialized_end=1102
  _globals['_FINDTICKERSUSREQUEST']._serialized_start=1105
  _globals['_FINDTICKERSUSREQUEST']._serialized_end=1301
  _globals['_FINDTICKERSUSRESPONSE']._serialized_start=1303
  _globals['_FINDTICKERSUSRESPONSE']._serialized_end=1365
  _globals['_TICKERSSERVICE']._serialized_start=1368
  _globals['_TICKERSSERVICE']._serialized_end=1745
# @@protoc_insertion_point(module_scope)
