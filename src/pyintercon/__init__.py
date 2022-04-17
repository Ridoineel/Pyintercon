# coding: utf-8;
#! /usr/bin/env python3

import socket
import signal
import sys
from json.encoder import JSONEncoder
from json.decoder import JSONDecoder
from .threads import ConnexionThread
from .threads import ResponseThread

json_encode = JSONEncoder().encode
json_decode = JSONDecoder().decode

class Server:
    """ This Server Object accept client and send response by her request,

    """

    def __init__(self):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # set exit signal function
        signal.signal(signal.SIGINT, Server.exit)

    def treatment(self, request_datas: dict) -> dict:
        """This function take request datas (dict) from client and return the
            response datas (dict)

            !!!!!!!! !!!!!!! DEFINED BY USER !!!!!! !!!!!!!
        """

        default_res = {"status": 1, "message": "default"}

        return default_res

    def handleResponse(self, request_datas: str) -> str:
        """ By treatment function, this function take string request_datas
            and return response (str)
        """

        containt = json_decode(request_datas)

        response_containt = self.treatment(containt)

        return json_encode(response_containt)

    def activate(self, ip: str, port: int):
        """ bind/activate server on @ip and @port,
            accept client, receve her request datas and
            manage the response

        """

        self.con.bind((ip, port))
        self.con.listen()

        # attribute localhost name to ip if
        # ip is empty
        if not ip: ip = 'localhost'

        print(f'Server is activated on {ip}:{port}...')
        print('Tap CTRL + C to quit !!!!!\n')

        clients_list = list()

        process1 = ConnexionThread(self.con, clients_list)
        process2 = ResponseThread(clients_list, self.handleResponse)
        
        process1.start()
        process2.start()

        process1.join()
        process2.join()

        self.con.close()

    @staticmethod
    def exit(signal, frame):
        print()
        print('Server is disconnected !!!')

        sys.exit(0)


class Client:

    def __init__(self):
        self.status = {"connected": False}
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip: str, port: int):
        if not self.status["connected"]:
            self.con.connect((ip, port))

            self.status["connected"] = True
        else:
            print('WARNING: Client is already connected...')

    def disconnect(self):
        if self.status["connected"]:

            self.con.close()

            self.status["connected"] = False
            return "disconnected"

        else:
            return  "not connected"


    def send(self, msg: dict) -> str:

        if self.status['connected']:

            containt = json_encode(msg)

            self.con.send(containt.encode())

            rep = self.con.recv(10**9)

            return json_decode( rep.decode() )

        else:
            print("WARNING: Client not connected !!!")


if __name__ == '__main__':
    print("""
        Class:
            Server: use to create server, accept client and answered client
            Client: use to connect to server and set request
    """)
