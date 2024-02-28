# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from finazon_grpc_python import datasets_pb2 as finazon__grpc__python_dot_datasets__pb2


class DatasetsServiceStub(object):
    """*
    DatasetsService provide access to Finazon datasets
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDatasets = channel.unary_unary(
                '/finazon.DatasetsService/GetDatasets',
                request_serializer=finazon__grpc__python_dot_datasets__pb2.GetDatasetsRequest.SerializeToString,
                response_deserializer=finazon__grpc__python_dot_datasets__pb2.GetDatasetsResponse.FromString,
                )


class DatasetsServiceServicer(object):
    """*
    DatasetsService provide access to Finazon datasets
    """

    def GetDatasets(self, request, context):
        """Get a list of all datasets available at Finazon.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatasetsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDatasets': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatasets,
                    request_deserializer=finazon__grpc__python_dot_datasets__pb2.GetDatasetsRequest.FromString,
                    response_serializer=finazon__grpc__python_dot_datasets__pb2.GetDatasetsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'finazon.DatasetsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatasetsService(object):
    """*
    DatasetsService provide access to Finazon datasets
    """

    @staticmethod
    def GetDatasets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/finazon.DatasetsService/GetDatasets',
            finazon__grpc__python_dot_datasets__pb2.GetDatasetsRequest.SerializeToString,
            finazon__grpc__python_dot_datasets__pb2.GetDatasetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)