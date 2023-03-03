import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.1.212'
host = socket.gethostname()
port = 444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    
    print("recieved connection from %s " % str(address))

    message = 'Hello, thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

   
    clientsocket.close()


