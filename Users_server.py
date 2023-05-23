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

from concurrent import futures
import logging

import grpc
import Users_pb2 as pb2
import Users_pb2_grpc as pb2_grpc

def check_string_in_tuples(my_list, search_string):
    for tup in my_list:
        if search_string in tup:
            return True
    return False

class Users(pb2_grpc.UsersServicer):

    users = list()
    cpt_id = 1

    def Register(self, request, context):
        if not check_string_in_tuples(self.users, request.username):
            user_info = (self.cpt_id, request.mail, request.username, request.password)
            self.users.append(user_info)
            self.cpt_id += 1
            print(self.users)
            return pb2.Response(code=1, message="User successfuly added")

        return pb2.Response(code=0, message="User already exists")

    def Login(self, request, context):
        for user in self.users:
            if user[2] == request.username:  
                if user[3] == request.password:  
                    return pb2.Response(code=1, message="Login successful.")
                else:
                    return pb2.Response(code=0, message="Incorrect password.")
        return pb2.Response(code=0, message="User not found.")


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
