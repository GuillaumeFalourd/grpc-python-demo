# gRPC Python

[This code's has been inspired from from the grpc.io site.](https://grpc.io/docs/languages/python/quickstart)

## Run

### Message

From the `python/message` directory:

Run the server:

```bash
python3 message_server.py
```

From another terminal window, run the client:

```bash
python3 message_client.py
```

### Demo

#### Sending message from client

![Client](/docs/img/message_client.png)

#### Logs from server

![Server](/docs/img/message_server.png)

## Update

### Message RPC code

Updating the `/protos/message.proto` file, we need to update the gRPC code used by our application to use the new service definition.

From the `message` directory, run:

```bash
python3 -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/message.proto
```
