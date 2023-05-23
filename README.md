# Distributed programming day 2

# Installation

## Requirements

Python >= 3.10

## Procédure (OS Linux)

```shell
# cd project/root/folder

# virtual environment creation
python -m venv venv

source venv/bin/activate

python -m pip install grpcio-tools
```

# Generate GRPC files for python

```sh
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. card.proto
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. users.proto
```

