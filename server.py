# coding: utf-8;

import socket
import signal
import sys
import threading

from json.encoder import JSONEncoder
from json.decoder import JSONDecoder

json_encode = JSONEncoder().encode
json_decode = JSONDecoder().decode

class Server:
    """ This Server Object accept client and send response by her request,

    *param: @nb_client: the number of client who will be connected to server

    """

    def __init__(self, nb_client: int = 1):
        self.nb_client = nb_client

    def treatment(self, request_datas: dict) -> dict:
        """This function take request datas (dict) from client and return the
            response datas (dict)

            !!!!!!!! !!!!!!! DEFINED BY USER !!!!!! !!!!!!!
        """

        default_res = {"status": 1, "message": "default"}

        return default_res

    def response(self, request_datas: str) -> str:
        """By treatment function, this function take request_datas on str type and return a correct
            response format (str)
        """

        containt = json_decode(request_datas)

        response_containt = self.treatment(containt)

        return json_encode(response_containt)

    def activate(self, ip: str, port: int):
        """ bind/activate server on @ip and @port,
            accept client, receve her request datas and
            manage the response

        """

        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.bind((ip, port))

        con.listen(self.nb_client)

        # attribute localhost name to ip if
        # ip is empty
        if not ip: ip = 'localhost'

        print(f'Server is activated on {ip}:{port}...')
        print('Tap CTRL + C to quit !!!!!\n')

        clients_list = list()

        for _ in range( self.nb_client ):
            # accept client
            client, param = con.accept()
            # set a client timeout for futur opération
            # on this: -> server waiting for receve request
            client.settimeout(.5)


            clients_list.append( (client, param) )

            print(f"\t{param} is connected ...")

        while True:

            for client, param in clients_list:
                try:
                    # receve request datas
                    req = client.recv(100).decode()
                    assert req

                except AssertionError:
                    clients_list.remove((client, param))
                    print(f"\t!!!! {param} is disconnected !!!!")
                except:
                    continue
                else:
                    rep = self.response(req)
                    client.send(str(rep).encode())

        con.close()

    @staticmethod
    def exit(signal, frame):
        print()
        print('Server is disconnected !!!')

        sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, Server.exit)

    sv = Server(2)
    sv.activate("", 8000)
