#!/usr/bin/env python3
from socket import *

s = socket(AF_INET, SOCK_STREAM)
# Establecer conexion con tupla -> (hostname, #port)
s.connect(("localhost", 9000))
# Enviamos una peticion
#s.send(b"GET /index.html HTTP/1.0\n\n")
# Enviamos un mensaje
s.send(b"Hola servidor, soy un cliente")
# Obtenemos la respuesta
data = s.recv(10000)
# Mostramos la data obtenida
print(repr(data))
# Cerramos la conexion
s.close()
