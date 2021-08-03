# gRPC (Google Remote Procedure Call) Python

[This code's has been inspired from from the grpc.io site.](https://grpc.io/docs/languages/python/quickstart)

## Run

### Message

#### Message Execution

From the `message` directory:

Run the server:

```bash
python3 message_server.py
```

From another terminal window, run the client:

```bash
python3 message_client.py
```

### Ritchie

#### Ritchie Premisse

- [Ritchie CLI](https://docs.ritchiecli.io/getting-started/install-cli) installed locally
- ritchie-formulas-demo Github repository imported:

```bash
rit add repo --provider="Github" --name="demo" --repoUrl="https://github.com/ZupIT/ritchie-formulas-demo" --priority=1
```

#### Ritchie Execution

From the `python/ritchie` directory:

Run the server:

```bash
python3 ritchie_server.py
```

From another terminal window, run the client:

```bash
python3 ritchie_client.py
```

## Demo

### Message Sample

#### Message inputs and response (client)

![Client](/docs/img/message_client.png)

#### Logs from message server

![Server](/docs/img/message_server.png)

### Ritchie Sample

#### Ritchie inputs and response (client)

![Client](/docs/img/ritchie_client.png)

#### Logs from ritchie server

![Server](/docs/img/ritchie_server.png)

## Update

### Message RPC code

Updating the `/protos/message.proto` file, we need to update the gRPC code used by our application to use the new service definition.

From the `message` directory, run:

```bash
python3 -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/message.proto
```

### Ritchie RPC code

Updating the `/protos/ritchie.proto` file, we need to update the gRPC code used by our application to use the new service definition.

From the `ritchie` directory, run:

```bash
python3 -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/ritchie.proto
```
