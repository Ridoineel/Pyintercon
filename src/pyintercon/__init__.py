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
    """ This server accepts clients and responds 
        to their request by a request processing function
        that you define by setRequestHandler method

        >>> sv = Server()
        >>> # set request handler
        >>> sv.setRequestHandler(your_handler_function)
        >>> 
        >>> # Now, activate server
        >>> sv.activate(("", 8080))
        Server is activated on localhost:8080...
        Tap CTRL + C to quit !!!!!


    """

    def __init__(self):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # set exit signal function
        signal.signal(signal.SIGINT, Server.exit)

    def _requestHandler(self, request_datas: dict) -> dict:
        """ This function take request data (dict) from client and return the
            response data (dict)

            !!!!!!!! DEFINED BY USER WITH setRequesthandler !!!!!!!
        """

        default_res = {"status": 1, "message": "default"}

        return default_res

    def handleResponse(self, request_datas: str) -> str:
        """ By requestHandler function, this function take string request data
            and return response (str)
        """

        containt = json_decode(request_datas)

        response_containt = self._requestHandler(containt)

        return json_encode(response_containt)

    def activate(self, ip: str, port: int):
        """ bind/activate server on @ip and @port,
            accept clients, receive their request data and
            manage the return of response

        """

        self.con.bind((ip, port))
        self.con.listen()

        clients_list = list()

        # attribute "localhost" to ip
        # if ip is empty
        if not ip: ip = 'localhost'

        print(f'Server is activated on {ip}:{port}...')
        print('Tap CTRL + C to quit !!!!!\n')

        process1 = ConnexionThread(self.con, clients_list)
        process2 = ResponseThread(clients_list, self.handleResponse)
        
        process1.start()
        process2.start()

        process1.join()
        process2.join()

        self.con.close()

    def setRequestHandler(self, function):
        if function:
            self._requestHandler = function
        else:
            raise ValueError("invalid function")

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
            Server: use to create server, accept clients and respond to their request
            Client: use to connect to a server and make requests 
    """)
