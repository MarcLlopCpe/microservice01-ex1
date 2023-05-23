"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging
import grpc
import Users_pb2 as pb2
import Users_pb2_grpc as pb2_grpc
from time import sleep


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.UsersStub(channel)

        responseRegister = stub.Register(pb2.RegisterCredentials(mail='test@test.test', username='totot', password='tutu'))
        print("register: " + str(responseRegister.code) + " " + responseRegister.message)

        sleep(1)

        responseLogin = stub.Login(pb2.Credentials(username='totot', password='tutu'))
        print("login: " + str(responseLogin.code) + " " + responseLogin.message)

if __name__ == '__main__':
    logging.basicConfig()
    run()
    