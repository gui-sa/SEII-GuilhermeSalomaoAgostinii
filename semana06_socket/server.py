#Server Side -  Centralize all clients and aplication control
#Router runs physics protocolls -> Modem transmits information to the world.
#Your modem has one IP address.. It is Public
#Behind Router there are Local IPs - NAT
#
#Extending for multiclients 


import socket
import threading #for message handling - IO Bound


HEADER = 64 #Bytes
PORT = 5050 #Port thta are not beeing used
SERVER = "127.0.0.1" #Local IP
SERVER = socket.gethostbyname(socket.gethostname())#get local ip address and use it as your server IP
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #first =  family (INET is IPV4) / SOCK_STREAM is for TCP 
server.bind(ADDR) #IP and PORT will be transfered to this aplication

def handle_client(conn , addr): #Handle individually each connection
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #blocking line of code. Args is a bytes number. decode is getting up the bytes and translating them into utf-8 - char.
        #Header will bring us how many bytes this messages brang
        #Header might not be big enought
        msg_length = int(msg_length) #string to int
        msg = conn.recv(msg_length).decode(FORMAT) #Now you receive yhe payload.
        # If you dont disconnect properly, the server might not accept same connection (because it is already connected). Due to that, it is important to sent a proper message to end a connection the right way
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] - {msg}" )
        conn.close() #disconnecting socket!


def start():#Allow Client to connect to our aplication and create a new thread to handle it
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while(True):
        conn, addr = server.accept() #That line blocks your code by waiting you client .. conn is a socket obj and addr is the information about the connection
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #Creating thread obj that handles that new client!
        thread.start()
        print(f"[ACTIVE CONNECTIONS: {threading.activeCount()-1}]")
print("[STARTING] Server is starting...")
start()









