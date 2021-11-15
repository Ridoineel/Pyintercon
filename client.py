# coding: utf-8;

import socket

from json.encoder import JSONEncoder
from json.decoder import JSONDecoder

json_encode = JSONEncoder().encode
json_decode = JSONDecoder().decode

class Client:

    def __init__(self):
        self.status = {"connected": False}
    
    def connect(self, ip: str, port: int):
        if not self.status["connected"]:
            self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

            rep = self.con.recv(1000)
    
            return json_decode( rep.decode() )

        else:
            print("WARNING: Client not connected !!!")
