# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobuf import train_pb2 as protobuf_dot_train__pb2


class TrainStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Training = channel.unary_unary(
                '/Train/Training',
                request_serializer=protobuf_dot_train__pb2.InputData.SerializeToString,
                response_deserializer=protobuf_dot_train__pb2.StatusCode.FromString,
                )


class TrainServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Training(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrainServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Training': grpc.unary_unary_rpc_method_handler(
                    servicer.Training,
                    request_deserializer=protobuf_dot_train__pb2.InputData.FromString,
                    response_serializer=protobuf_dot_train__pb2.StatusCode.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Train', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Train(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Training(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Train/Training',
            protobuf_dot_train__pb2.InputData.SerializeToString,
            protobuf_dot_train__pb2.StatusCode.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
