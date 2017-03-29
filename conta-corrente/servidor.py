#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 6006
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
resposta = None

if not len(sys.argv) >= 2:
    print ("[SERVIDOR][ERRO] O valor do saldo deve ser informado.")
    sys.exit(-1)

saldo = int(sys.argv[1])
print ("[SERVIDOR][INFO] Saldo inicial:", saldo)

print ("[SERVIDOR] Abrindo a porta " + str(TCP_PORT) + " e ouvindo")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print ("[SERVIDOR] Aguardando conexao")
conn, addr = s.accept()
print ('[SERVIDOR] Conexao com o cliente realizada. Endereco da conexao:', addr)
while 1:
    print ("[SERVIDOR] Aguardando dados do cliente")
    operacao = conn.recv(BUFFER_SIZE).decode("utf-8")
    if not operacao: break
    print ("[SERVIDOR] Dados recebidos do cliente com sucesso: \"" + operacao + "\"")
    
    # TODO interpretar a operacao
    # ... 
    # TODO alterar saldo se necessario
    # ...
    
    resposta = str(saldo)

    print ("[SERVIDOR] Enviando resposta para o cliente")
    conn.send(resposta.encode())  # echo
    print ("[SERVIDOR] Resposta enviada: \"" + resposta + "\"")
print ("[SERVIDOR] Fechando a porta " + str(TCP_PORT))
conn.close()
print ("[SERVIDOR] Fim")
