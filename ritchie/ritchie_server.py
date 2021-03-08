"""The Python implementation of the GRPC ritchie.Ritchie server."""

from concurrent import futures
import logging
import grpc
import os
import ritchie_pb2
import ritchie_pb2_grpc


class Ritchie(ritchie_pb2_grpc.RitchieServicer):

    def Ritchie(self, request, context):
        ## Build rit demo hello-world formula command with input flags
        print(f"\033[36m🛠  Ritchie server formula command from inputs:\033[0m")
        command = f"rit demo hello-world --rit_input_text=\"{request.name}\" --rit_input_boolean={request.boolean} --rit_input_list=\"{request.automate}\" --rit_input_password=\"{request.text}\""
        print(command)
        print(f"\033[36m⚙️  Ritchie server executing formula command\033[0m")
        message = os.popen(f"{command}").read()
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
