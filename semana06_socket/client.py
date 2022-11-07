import socket

HEADER = 64 #Bytes
PORT = 5060 #Port thta are not beeing used
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONECT" 
SERVER = "127.0.1.1" #Ip do meu servidor
ADDR= (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Abrindo um socket do tipo tcp para IPV4

client.connect(ADDR) #Conectando na porta e no IP combionado do servidor

def send(msg):
    message = msg.encode(FORMAT) #transformar string em Bytes par enviar
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) #A primeira informacao a ser enviada eh o comprimento da mensagem como um todo.
    #Nao necessariamente sabemos se ele esta dentro ou nao do legth de 64
    send_length += b' ' *(HEADER - len(send_length)) #Vamos concatenar a mensagem que manda o numero de nadas em byte  para garantir que enviara obrigatoriamente 64 bytes
    client.send(send_length)
    client.send(message)


send("Hello")
send(DISCONNECT_MESSAGE)