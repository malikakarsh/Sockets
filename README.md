# Sockets
Programas com exemplo de comunicação entre programas utilizando sockets.


## Echo
Com o PATH configurado corretamente (veja abaixo como configurar),  inicie o servidor e depois o cliente em dois terminais distintos.

No terminal 1, do servidor:
```CMD
python3 echo/servidor.py
```

No terminal 2, do cliente:
```CMD
python3 echo/cliente.py
```

O resultado esperado é:

No terminal 1, do servidor:

```CMD
('Connection address:', ('127.0.0.1', 51451))
('received data:', 'Hello, World!')
```

No terminal 2, do cliente:
```CMD
('received data:', 'Hello, World!')
```

---------------------------------
Para utilizar o servidor de echo você precisa do Interpretador Python instalado e, no Windows, que sua variável de ambiente PATH aponte corretamente para a pasta onde o Python está instalado. 

Considerando que o Python esteja instalado em "C:\Python27\" e que o PATH não contenha esse fragmento, para adicionar o Python ao PATH no Prompt de Comando do Windows, digite o seguinte comando:

```CMD
```
