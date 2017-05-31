#!/usr/bin/env python
# -*- coding: utf-8 -*-

# adaptado de https://wiki.python.org/moin/TcpCommunication

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
NOME = "Javalisson"

print ("[CLIENTE] Iniciando")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("[CLIENTE] Conectando")
s.connect((TCP_IP, TCP_PORT))
print ("[CLIENTE] Enviando dados: \"" + NOME + "\"")
s.send(NOME.encode('utf-8'))
print ("[CLIENTE] Recebendo dados do servidor")
resposta = s.recv(BUFFER_SIZE)
print ("[CLIENTE] Dados recebidos em resposta do servidor: \"" + resposta.decode('utf-8') + "\"")
print ("[CLIENTE] Fechando conexão com o servidor")
s.close()

print ("[CLIENTE] Fim")