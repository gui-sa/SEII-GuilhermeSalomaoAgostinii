#Server UDP
import socket
import select

UDP_IP = "127.0.0.1" #Ip do servidor - Local
IN_PORT = 5005 #Porta para recepcao de dados
timeout = 3 #3 segundos maximos de espera


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPV4 UDP
sock.bind((UDP_IP, IN_PORT)) #Se receber algo nesse IP, nessa porta, mandar para essa aplicacao

while True: #Loop Infinito
    data, addr = sock.recvfrom(1024) #Leio, quando tiver, 1024 Bytes
    if data: #Se tiver dados...
        print ("File name:", data)#Printo
        file_name = data.strip()#Faco nada com strings ... rs

    f = open(file_name, 'wb') #Abro um arquivo com o nome que foi transmitido na forma de escrita de bytes

    while True:# Loop infinito
        ready = select.select([sock], [], [], timeout) #Ele aguarda operacoes de IO... se nao receber, aguarda um maximo de timeout
        if ready[0]: #Se tiver algo na lista do ready
            data, addr = sock.recvfrom(1024) #Leia!
            f.write(data)#Escreve no arquivo aberto
        else:
            print ("%s Finish!" % file_name) #Se nao tiver nada, ou timeout, ele finaliza
            f.close()
            break