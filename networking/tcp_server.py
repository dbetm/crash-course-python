#!/usr/bin/env python3

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(("",9000))
s.listen(5) # 5 es el máximo número de clientes que podrá escuchar

# Proceso de escuchar
while True:
    client, address= s.accept()
    print("Received connection from", address)
    data = client.recv(10000)
    print(repr(data))
    # Respondemos
    string = "Hola " + str(address[0])
    client.send(str.encode(string))
    # Cerramos la conexión
    client.close()
