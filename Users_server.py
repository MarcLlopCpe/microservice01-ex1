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
"""The Python implementation of the GRPC helloworld.Greeter server."""

import logging
from concurrent import futures

import grpc

import users_pb2 as pb2
import users_pb2_grpc as pb2_grpc
from models.User_model import User_model


def check_string_in_tuples(my_list, search_string):
    for tup in my_list:
        if search_string in tup:
            return True
    return False


class users(pb2_grpc.usersServicer):
    users = []
    cpt_id = 1

    def Register(self, request, context):
        """
        Assure la création des utilisateurs
        :param request:
        :param context:
        :return:
        """

        if not check_string_in_tuples(self.users, request.username):
            user_info = User_model(
                self.cpt_id, request.mail, request.username, request.password
            )

            self.users.append(user_info)
            self.cpt_id += 1
            return pb2.Response(code=1, message="User successfully added")

        return pb2.Response(code=0, message="User already exists")

    def Login(self, request, context):
        """
        Assure l'authentification de l'utilisateur
        :param request:
        :param context:
        :return:
        """
        for user in self.users:
            if user.authenticate(request.username, request.password):
                return pb2.Response(code=1, message="Login successful")
            else:
                return pb2.Response(code=0, message="Incorrect password")
        return pb2.Response(code=0, message="User not found")

    def AddCard(self, request, context):
        """
        Ajoute une card à un utilisateur (seulement en mémoire vive)
        :param request:
        :param context:
        :return:
        """
        for user in self.users:
            if user.username == request.username:
                user.add_pokemon_card(
                    pb2.Carda(
                        id=request.id,
                        name=request.name,
                        health=request.health,
                        attack=request.attack,
                        defense=request.defense
                    )
                )
                return pb2.Response(code=1, message="Successfully added card to user " + user.username + ".")

    def GetUser(self, request, context):
        for user in self.users:
            if user.username == request.username:
                return pb2.UserResponse(username=user.username, result=user.pokemon_cards)


def serv():
    port = '50051'

    # Création d'un pool de thread pour assurer le traitement des requêtes au serveur
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))

    # Accrochement d'un service au server /!\ On aurait pu accrocher plusieurs services à celui-ci
    pb2_grpc.add_usersServicer_to_server(users(), server)

    # définition du port
    server.add_insecure_port('[::]:' + port)

    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serv()
