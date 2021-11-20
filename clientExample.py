# coding: utf-8;
from pyintercon import Client

host_ip = "localhost"
port = 8080

cl = Client()
cl.connect(host_ip, port)

res = cl.send({"message": "Hello World !"})

print(res)
