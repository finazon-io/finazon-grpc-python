# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from finazon_grpc_python import snapshot_pb2 as finazon__grpc__python_dot_snapshot__pb2


class SnapshotServiceStub(object):
    """*
    SnapshotService provide access to ticker snapshot
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSnapshot = channel.unary_unary(
                '/finazon.SnapshotService/GetSnapshot',
                request_serializer=finazon__grpc__python_dot_snapshot__pb2.GetSnapshotRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_snapshot__pb2.GetSnapshotResponse.FromString,
                )


class SnapshotServiceServicer(object):
    """*
    SnapshotService provide access to ticker snapshot
    """

    def GetSnapshot(self, request, context):
        """This endpoint returns a combination of different data points, such as daily performance, last quote, last trade, minute data, and previous day performance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SnapshotServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSnapshot,
                    request_deserializer=finazon__grpc__python_dot_snapshot__pb2.GetSnapshotRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_snapshot__pb2.GetSnapshotResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'finazon.SnapshotService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SnapshotService(object):
    """*
    SnapshotService provide access to ticker snapshot
    """

    @staticmethod
    def GetSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.SnapshotService/GetSnapshot',
            finazon__grpc__python_dot_snapshot__pb2.GetSnapshotRequest.SerializeToString,
            finazon__grpc__python_dot_snapshot__pb2.GetSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
