from socket import *
# Tipos de IP
    # AF_INET, para IPv4
    # AF_INET6, para IPv6
# Protocolos empleados en los sockets
    # .SOCK_STREAM (TCP)
    # .SOCK_DGRAM (UDP)

s1 = socket(AF_INET, SOCK_STREAM) # Más común
s2 = socket(AF_INET, SOCK_DGRAM)
