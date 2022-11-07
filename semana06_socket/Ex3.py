#Client UDP
import socket
import time
import sys

UDP_IP = "127.0.0.1" #IP do servidor - LOCAL
UDP_PORT = 5005 #Porta de envio das informacoes
buf = 1024 #Numero maximo de envio de bytes por vez
file_name = sys.argv[1] #Primeiro argumento sem ser o comando todo


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPV4 UDP
sock.sendto(file_name.encode('utf-8'), (UDP_IP, UDP_PORT)) #Enviando para o servidor, na porta do servidor, os bytes que significam o nome do arquivo
print ("Sending %s ..." % file_name)

f = open(file_name, "rb") #Leitura como Bytes
data = f.read(buf) #Leitura do numero maximo decidido de bytes
while(data): #Loop que dura ate ter informacao par enviar com base no ponteiro do arquivo
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): #Se quando enviar para o servidor, for um sucesso:
        data = f.read(buf) #Leio o proximo chunk de dados
        time.sleep(0.02) # Espera um pouco para nao afogar o servidor

sock.close()#Fecha o socket
f.close()# Fecha o arquivo de leitura