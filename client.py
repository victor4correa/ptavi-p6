#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Programa cliente que abre un socket a un servidor."""

import socket
import sys
# Cliente UDP simple.

# Dirección IP del servidor.
try:
    METHOD = sys.argv[1]
    USER = sys.argv[2].split(":")[0]
    PORT = sys.argv[2].split(":")[1]
    SERVER = USER.split("@")[1]

    # Contenido que vamos a enviar
    LINE = (METHOD + " sip:" + USER + " SIP/2.0\r\n")

except IndexError:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, int(PORT)))

    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print(data.decode('utf-8'))
    if METHOD == "INVITE":
        my_socket.send(bytes("ACK sip:" + USER + " SIP/2.0", "utf-8")
                       + b'\r\n')
        data = my_socket.recv(1024)
    print("Fin.")
