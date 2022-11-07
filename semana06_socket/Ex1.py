#CLIENTE TCP
import socket
import sys

TCP_IP = "127.0.0.1" #Ip do servidor... Local
FILE_PORT = 5005 # Porta para envio do nome do arquivo
DATA_PORT = 5006 #Porta para envio da informacao util
buf = 1024 #Numero maximo de bytes a ser enviado por vez
file_name = sys.argv[1] #primeira string sem ser o proprio comando todo... Chamado usando python Ex1.py NomeDoArquivo. Lembrando que o server tem que estar de pe

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP IPV4
    sock.connect((TCP_IP, FILE_PORT)) #Conectando para o servido usando a porta do arquivo primeiro
    sock.send(file_name.encode('utf_8')) #Envia o nome do arquivo... Esse nome do arquivo tem que estar em Bytes.
    sock.close() #Fecha o socket

    print ("Sending %s ..." % file_name)

    f = open(file_name, "rb") #Abre o arquivo como leitura em bytes
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4 TCP
    sock.connect((TCP_IP, DATA_PORT)) #EAbre o socket na porta DATA
    data = f.read() #Le TODO o conteudo do arquivo ... Cuidado com o buffer! Cuidado com a memoria
    sock.send(data) #Envia os dados lidos

finally:
    sock.close() #Se surgir algum error, ele fecha tudo para garantir que nao vai vazar memoria.
    f.close() 