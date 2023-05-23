#!/usr/bin/env bash

CARD_OUT="."

python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. card.proto
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. users.proto
