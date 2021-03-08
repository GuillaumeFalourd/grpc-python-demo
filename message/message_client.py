"""The Python implementation of the GRPC message.Message client."""

import logging
import grpc
import os
import message_pb2
import message_pb2_grpc


def run():
    
    # Configure channel
    channel = grpc.insecure_channel('localhost:50051')
    stub = message_pb2_grpc.MessageStub(channel)
    
    # Ask for inputs
    text = input("Enter the text to send: ") 
    name = input("Enter your name: ") 
    surname = input("Enter your surname: ") 
    
    command = f"rit demo hello-world --rit_input_text={name} --rit_input_boolean=true --rit_input_list=everything --rit_input_password={text}"
    os.system(f"{command}")
    
    # Call the Message method from the message.proto file
    response = stub.Message(message_pb2.MessageRequest(text=text, name=name, surname=surname))
    print("Message client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
