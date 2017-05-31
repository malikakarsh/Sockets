#!/usr/bin/env python
# -*- coding: utf-8 -*-

# adaptado de https://wiki.python.org/moin/TcpCommunication

import socket

TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

print ("[SERVIDOR] Iniciando")

print ("[SERVIDOR] Abrindo a porta " + str(TCP_PORT) + " e ouvindo")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print ("[SERVIDOR] Aguardando conexao")
conn, addr = s.accept()
print ('[SERVIDOR] Conexao com o cliente realizada. Endereco da conexao:', addr)
while 1:
    print ("[SERVIDOR] Aguardando dados do cliente")
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("[SERVIDOR] Dados recebidos do cliente com sucesso: \"" + data.decode('utf-8') + "\"")
    print ("[SERVIDOR] Enviando resposta para o cliente")
    conn.send(data)  # echo
    print ("[SERVIDOR] Resposta enviada: \"" + data.decode('utf-8') + "\"")
print ("[SERVIDOR] Fechando a porta " + str(TCP_PORT))
conn.close()
print ("[SERVIDOR] Fim")
