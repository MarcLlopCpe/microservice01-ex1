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
import pathlib
from concurrent import futures

import grpc

import card_pb2 as pb2
import card_pb2_grpc as pb2_grpc

RES_PATH = pathlib.Path("./data")
RES_CARD = RES_PATH / pathlib.Path("pokemon.csv")


def _read_pokemons(path=RES_CARD, header_selector=(0, 1, 5, 6, 7)):
    """
    Lecture du csv de pokemon et transformation en liste en utilisant seulement les indices contenu dans header_selector

    :param path: chemin du fichier csv
    :param header_selector: indice à récupérer
    :return:
    """
    import csv

    ret = []
    with open(path) as f:
        c = csv.reader(f, )

        header = c.__next__()

        for line in c:
            row = {}

            for i in header_selector:
                row[header[i]] = line[i]

            ret.append(row)

    return ret


class Cards(pb2_grpc.Card):
    full_card_list = _read_pokemons()
    id_card_list = [int(card["id"]) for card in full_card_list]

    def getCards(self, request, context, *args, **kwargs):
        """
        Renvoi une liste d'id de cartes
        :param request:
        :param context:
        :param args:
        :param kwargs:
        :return:
        """
        return pb2.IdCardsResponse(result=self.id_card_list)

    def getFullCard(self, request, context, *args, **kwargs):
        """
        Renvoi une carte "complète"
        :param request:
        :param context:
        :param args:
        :param kwargs:
        :return:
        """
        ret = self.full_card_list[request.id]
        return pb2.FullCard(**ret)


def serv():  # idem que l'autre serveur
    port = '50052'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    pb2_grpc.add_CardServicer_to_server(Cards(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()  # Utilisation du système de log type unix
    serv()
