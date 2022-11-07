#SERVIDOR TCP
import socket

TCP_IP = "127.0.0.1" #Ip do server
FILE_PORT = 5005 #Porta que recebera o arquivo
DATA_PORT = 5006 #Porta que recebera informações
timeout = 3 #Tempo de espera maxima para cada envio
buf = 1024 #Numero de bytes por pacote recebido por vez


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4 TCP
sock_f.bind((TCP_IP, FILE_PORT)) #Tudo que a placa de rede com Ip designado e porta de arquivo, vira para essa aplicacao
sock_f.listen(1) #Ouve por um cliente

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT)) 
sock_d.listen(1)
#Ele conecta ambos os sockets aceitando apenas um cliente... Se o cliente falhar em alugma solicitação, o server trava.

while True: #loop infinito
    conn, addr = sock_f.accept() #Aceita a conexao conn eh obj de conexao e addr eh informacao da conexao
    data = conn.recv(buf) #Recebe o numero maximo de bytes = buff 
    if data:
        print ("File name:", data) #Se tiver algo, printa o nome do arquivo
        file_name = data.strip() #Não tira nada da string...

    f = open(file_name, 'wb') #Abre o arquivo com o nome recebido no modo escrita binaria 


    conn, addr = sock_d.accept() 
    while True:
        data = conn.recv(buf) 
        if not data: #Enquanto tiver dados para ler, continua... quando acabar, sai do while.
            break
        f.write(data)

    print ("%s Finish!" % file_name)
    f.close()