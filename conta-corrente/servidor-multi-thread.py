#!/usr/bin/env python
# -*- coding: utf-8 -*-

# adaptado de https://wiki.python.org/moin/TcpCommunication

import sys
import threading
import socket

TCP_IP = ''
TCP_PORT = 7007
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

saldo = 0
operacoes = []

if len(sys.argv) >= 2:
    saldo = int(sys.argv[1])

print ("[SERVIDOR][INFO] Saldo inicial:", saldo)


def atende_cliente(conn, addr):
    global saldo
    global operacoes
    while 1:
        msg = ''
        dados = bytearray()
        print ("[SERVIDOR ", addr, "] Aguardando dados do cliente")
        fim_msg = False
        try:
            while not fim_msg:
                recvd = conn.recv(BUFFER_SIZE)
                if not recvd:
                    raise ConnectionError()
                    break
                dados += recvd
                print ("[SERVIDOR ", addr, "] Recebidos ", len(recvd), " bytes")
                if b'\n' in recvd:
                    msg = dados.rstrip(b'\n').decode('utf-8')
                    fim_msg = True
            print ("[SERVIDOR ", addr, "] Recebidos no total ", len(dados), " bytes")
            print ("[SERVIDOR ", addr, "] Dados recebidos do cliente com sucesso: \"" + msg + "\"")

            # interpretar a dados
            comando = msg.split(' ')
            operacao = comando[0]
            if operacao == 'SALDO':
                resposta = str(saldo)
            elif operacao == 'EXTRATO':
                resposta = ''
                primeiro = True
                for op in operacoes:
                    if primeiro:
                        primeiro = False
                        resposta += str(op)
                    else:
                        resposta += "," + str(op)

            elif operacao == 'DEBITO':
                valor = int(comando[1])
                saldo -= valor
                operacoes.append(-valor)
                resposta = str(saldo)
            elif operacao == 'CREDITO':
                valor = int(comando[1])
                saldo += valor
                operacoes.append(valor)
                resposta = str(saldo)
            else: 
                resposta = 'ERRO'

            print ("[SERVIDOR ", addr, "] Enviando resposta para o cliente")
            conn.send((resposta + '\n').encode('utf-8'))  # echo
            print ("[SERVIDOR ", addr, "] Resposta enviada: \"" + resposta + "\"")
        except BaseException as erro:
            print ("[SERVIDOR ", addr, "] [ERROR] Socket error: ", erro)
            break
    print ("[SERVIDOR ", addr, "] Fechando a conexao ", addr)
    conn.close()

print ("[SERVIDOR] Iniciando")

print ("[SERVIDOR] Abrindo a porta " + str(TCP_PORT) + " e ouvindo")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while 1:
    print ("[SERVIDOR] Aguardando conexao")
    conn, addr = s.accept()
    thread = threading.Thread(target=atende_cliente,
                              args=[conn, addr],
                              daemon=True)
    thread.start()
    print ("[SERVIDOR ", addr, "] Conexao com o cliente realizada. Endereco da conexao:", addr)    

print ("[SERVIDOR] Fechando a porta " + str(TCP_PORT))
s.close()

print ("[SERVIDOR] fim_msg")
