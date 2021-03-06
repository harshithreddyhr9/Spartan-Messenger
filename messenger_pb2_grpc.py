# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import messenger_pb2 as messenger__pb2


class MessengerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.MsgStream = channel.unary_stream(
        '/Messenger/MsgStream',
        request_serializer=messenger__pb2.EmptyStream.SerializeToString,
        response_deserializer=messenger__pb2.Msg.FromString,
        )
    self.SendMsg = channel.unary_unary(
        '/Messenger/SendMsg',
        request_serializer=messenger__pb2.Msg.SerializeToString,
        response_deserializer=messenger__pb2.EmptyStream.FromString,
        )


class MessengerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def MsgStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendMsg(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessengerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'MsgStream': grpc.unary_stream_rpc_method_handler(
          servicer.MsgStream,
          request_deserializer=messenger__pb2.EmptyStream.FromString,
          response_serializer=messenger__pb2.Msg.SerializeToString,
      ),
      'SendMsg': grpc.unary_unary_rpc_method_handler(
          servicer.SendMsg,
          request_deserializer=messenger__pb2.Msg.FromString,
          response_serializer=messenger__pb2.EmptyStream.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Messenger', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
