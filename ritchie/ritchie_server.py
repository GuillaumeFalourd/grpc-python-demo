"""The Python implementation of the GRPC ritchie.Ritchie server."""

from concurrent import futures
import logging
import grpc
import os
import ritchie_pb2
import ritchie_pb2_grpc


class Ritchie(ritchie_pb2_grpc.RitchieServicer):

    def Ritchie(self, request, context):
        print(f"\033[36mRitchie server received formula command:\033[0m\n {request.command}")
        print(f"\033[36m⚙️  Ritchie server executing formula command\033[0m")
        message = os.popen(f"{request.command}").read()
        print(f"\033[36m✅ Ritchie server sent formula response\033[0m")
        return ritchie_pb2.RitchieReply(message=f'{message}')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ritchie_pb2_grpc.add_RitchieServicer_to_server(Ritchie(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
