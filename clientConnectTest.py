# coding: utf-8;
import socket

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

con.connect(("", 80))

def send(msg) -> str:

    con.send(str(msg).encode())

    rep = con.recv(100)
  
    return rep.decode()

while 1:
    rep = send(input())
    print(rep)
    
con.close()