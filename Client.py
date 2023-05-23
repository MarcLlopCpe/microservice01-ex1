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

import card_pb2
import card_pb2_grpc
import users_pb2
import users_pb2_grpc


def run():
    cards = []

    with grpc.insecure_channel('localhost:50052') as channel:
        card_stub = card_pb2_grpc.CardStub(channel)
        ids = card_stub.getCards(card_pb2.Empty())

        for i in ids.result:
            card: card_pb2.FullCard = card_stub.getFullCard(card_pb2.SimpleCard(id=i))
            cards.append(card)
            print(card)

    with grpc.insecure_channel('localhost:50051') as channel:
        users_stub = users_pb2_grpc.usersStub(channel)

        response_register = users_stub.Register(users_pb2.RegisterCredentials(
            mail='test@test.test', username='totot', password='tutu'))
        print("register: " + str(response_register.code) +
              " " + response_register.message)

        response_login = users_stub.Login(users_pb2.Credentials(
            username='totot', password='tutu'))
        print("login: " + str(response_login.code) + " " + response_login.message)

        response_add_card = users_stub.AddCard(
            users_pb2.AddCardRequest(username='totot', id='1', name='Bulbasaur', health='45', attack='49',
                                     defense='49'))
        print("add card: ", str(response_login.code), " ", response_login.message)

        response_get_user = users_stub.GetUser(users_pb2.Credentials(
            username='totot', password='tutu'))
        print("add card: ", str(response_login.code), " ", response_login.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
