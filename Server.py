#Create a chat app with a server and client
#our server will handle many clients 
#the client connects to the server
#the server distributes the messages to everyone
# we shall handle multiple connections

import socket
import select

#Constants
HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

#making the sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

#clients dictionary(directory)
clients = {}

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        #if not message was received
        if not len(message_header):
            return False

        #if a message was received
        message_length = int(message_header.decode("utf-8").strip())
        return {
                    "header":message_header, 
                    "data":client_socket.recv(message_length)
                }

    except:
        return False

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            #if someone just connected and we need to handle for that
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)

            if(user is False):
                #user disconnected
                continue

            #if a user just connected
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
        
        else:
            message = receive_message(notified_socket)


            if(message is False):
                #if the user is disconnected, removed them from the list and del the user
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f"Received message from {user['data'].decode('utf-8')}:{message['data'].decode('utf-8')}")

            #share the message that we just got with everybody 
            for client_socket in clients:
                if client_socket !=notified_socket:
                    #if the user is not the sender then send it to them
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
