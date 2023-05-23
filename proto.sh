#!/usr/bin/env bash

CARD_OUT="."

python -m grpc_tools.protoc -I./protos --python_out=$CARD_OUT --pyi_out=$CARD_OUT --grpc_python_out=$CARD_OUT card.proto
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. users.proto
