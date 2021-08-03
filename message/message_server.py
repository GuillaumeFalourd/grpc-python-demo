"""The Python implementation of the GRPC message.Message server."""

from concurrent import futures
import logging
import grpc
import message_pb2
import message_pb2_grpc


class Message(message_pb2_grpc.MessageServicer):

    def Message(self, request, context):
        print(f"Client sent a message from {request.name} {request.surname}")
        return message_pb2.MessageReply(message=f'I received the message \"{request.text}\" from {request.name} {request.surname}')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessageServicer_to_server(Message(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
