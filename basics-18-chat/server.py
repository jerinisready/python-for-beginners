import socket
import select
from thread import *
import sys

if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(100)
list_of_clients=[]


def clientthread(conn, addr):
    conn.send("Hi, Welcome to this chatroom!")
    #sends a message to the client whose user object is conn
    while True:
            try:
                message = conn.recv(2048)
                if message:
                    print message
                    message_to_send = message
                    broadcast(message_to_send,conn)
                    #prints the message and address of the user who just sent the message on the server terminal
                else:
                    remove(conn)
            except:
                continue

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients != connection:   # Send Message to Everyone other than Sender
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
        broadcast(connection + " Left The Group!",connection)
while True:
    conn, addr = server.accept()
    """
    Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
    the IP address of the client that just connected
    """
    list_of_clients.append(conn)
    print addr[0] + " connected"
    #maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
    #Prints the address of the person who just connected
    start_new_thread(clientthread,(conn,addr))
    #creates and individual thread for every user that connects

conn.close()
server.close()
