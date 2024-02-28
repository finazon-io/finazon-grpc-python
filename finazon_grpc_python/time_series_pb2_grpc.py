# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from finazon_grpc_python import time_series_pb2 as finazon__grpc__python_dot_time__series__pb2


class TimeSeriesServiceStub(object):
    """*
    TimeSeriesService provide access to time series data
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTimeSeries = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeries',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesResponse.FromString,
                )
        self.GetTimeSeriesAtr = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeriesAtr',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesAtrRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesAtrResponse.FromString,
                )
        self.GetTimeSeriesBBands = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeriesBBands',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesBBandsRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesBBandsResponse.FromString,
                )
        self.GetTimeSeriesIchimoku = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeriesIchimoku',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesIchimokuRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesIchimokuResponse.FromString,
                )
        self.GetTimeSeriesMa = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeriesMa',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMaRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMaResponse.FromString,
                )
        self.GetTimeSeriesMacd = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeriesMacd',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMacdRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMacdResponse.FromString,
                )
        self.GetTimeSeriesObv = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeriesObv',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesObvRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesObvResponse.FromString,
                )
        self.GetTimeSeriesRsi = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeriesRsi',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesRsiRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesRsiResponse.FromString,
                )
        self.GetTimeSeriesSar = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeriesSar',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesSarRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesSarResponse.FromString,
                )
        self.GetTimeSeriesStoch = channel.unary_unary(
                '/finazon.TimeSeriesService/GetTimeSeriesStoch',
                request_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesStochRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesStochResponse.FromString,
                )


class TimeSeriesServiceServicer(object):
    """*
    TimeSeriesService provide access to time series data
    """

    def GetTimeSeries(self, request, context):
        """Get time series data without technical indicators
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSeriesAtr(self, request, context):
        """Get time series data for ATR technical indicator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSeriesBBands(self, request, context):
        """Get time series data for BBands technical indicator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSeriesIchimoku(self, request, context):
        """Get time series data for Ichimoku technical indicator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSeriesMa(self, request, context):
        """Get time series data for Ma technical indicator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSeriesMacd(self, request, context):
        """Get time series data for Macd technical indicator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSeriesObv(self, request, context):
        """Get time series data for Obv technical indicator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSeriesRsi(self, request, context):
        """Get time series data for Rsi technical indicator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSeriesSar(self, request, context):
        """Get time series data for Sar technical indicator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSeriesStoch(self, request, context):
        """Get time series data for Stoch technical indicator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TimeSeriesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTimeSeries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeries,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesResponse.SerializeToString,
            ),
            'GetTimeSeriesAtr': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeriesAtr,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesAtrRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesAtrResponse.SerializeToString,
            ),
            'GetTimeSeriesBBands': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeriesBBands,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesBBandsRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesBBandsResponse.SerializeToString,
            ),
            'GetTimeSeriesIchimoku': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeriesIchimoku,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesIchimokuRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesIchimokuResponse.SerializeToString,
            ),
            'GetTimeSeriesMa': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeriesMa,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMaRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMaResponse.SerializeToString,
            ),
            'GetTimeSeriesMacd': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeriesMacd,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMacdRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMacdResponse.SerializeToString,
            ),
            'GetTimeSeriesObv': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeriesObv,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesObvRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesObvResponse.SerializeToString,
            ),
            'GetTimeSeriesRsi': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeriesRsi,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesRsiRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesRsiResponse.SerializeToString,
            ),
            'GetTimeSeriesSar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeriesSar,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesSarRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesSarResponse.SerializeToString,
            ),
            'GetTimeSeriesStoch': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSeriesStoch,
                    request_deserializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesStochRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesStochResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'finazon.TimeSeriesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TimeSeriesService(object):
    """*
    TimeSeriesService provide access to time series data
    """

    @staticmethod
    def GetTimeSeries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeries',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSeriesAtr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeriesAtr',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesAtrRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesAtrResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSeriesBBands(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeriesBBands',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesBBandsRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesBBandsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSeriesIchimoku(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeriesIchimoku',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesIchimokuRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesIchimokuResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSeriesMa(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeriesMa',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMaRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSeriesMacd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeriesMacd',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMacdRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesMacdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSeriesObv(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeriesObv',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesObvRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesObvResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSeriesRsi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeriesRsi',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesRsiRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesRsiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSeriesSar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeriesSar',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesSarRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesSarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSeriesStoch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.TimeSeriesService/GetTimeSeriesStoch',
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesStochRequest.SerializeToString,
            finazon__grpc__python_dot_time__series__pb2.GetTimeSeriesStochResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)