#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        line = self.rfile.read().decode('utf-8')
        contenido = line.split()
        print("El cliente nos manda " + line)
        if contenido[0] == "INVITE":
            self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n" 
                              + b"SIP/2.0 180 Ringing\r\n\r\n"
                              + b"SIP/2.0 200 OK\r\n")
        
if __name__ == "__main__":
    
    PORT = sys.argv[2]
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', int(PORT)), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
