# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc

import card_pb2 as pb2
import card_pb2_grpc as pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.CardStub(channel)
        ids: pb2.IdCardsResponse = stub.getCards(pb2.Empty())

        for i in ids.result:
            card: pb2.FullCard = stub.getFullCard(pb2.SimpleCard(id=i))
            print(card)


if __name__ == '__main__':
    logging.basicConfig()
    run()
