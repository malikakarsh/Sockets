#!/usr/bin/env python
# -*- coding: utf-8 -*-

# adaptado de https://wiki.python.org/moin/TcpCommunication

import sys
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20
MESSAGE = "Olá Mundo!"

if len(sys.argv) >= 2:
    TCP_IP = sys.argv[1]

if len(sys.argv) >= 3:
    MESSAGE = sys.argv[2]

print ("[CLIENTE] Iniciando")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("[CLIENTE] Conectando")
s.connect((TCP_IP, TCP_PORT))
print ("[CLIENTE] Enviando dados: \"" + MESSAGE + "\"")
s.send((MESSAGE + '\n').encode('utf-8'))
print ("[CLIENTE] Recebendo dados do CLIENTE")
msg = ''
fim_msg = False
dados = bytearray()
while not fim_msg:
	recvd = s.recv(BUFFER_SIZE)
	dados += recvd
	print ("[CLIENTE] Recebidos ", len(recvd), " bytes")
	if b'\n' in recvd:
		msg = dados.rstrip(b'\n').decode('utf-8')
		fim_msg = True
print ("[CLIENTE] Recebidos no total ", len(dados), " bytes")
print ("[CLIENTE] Dados recebidos em resposta do CLIENTE: \"" + msg + "\"")
print ("[CLIENTE] Fechando conexão com o CLIENTE")
s.close()

print ("[CLIENTE] Fim")
