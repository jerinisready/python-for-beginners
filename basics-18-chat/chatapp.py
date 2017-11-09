import socket
import select
import sys

if len(sys.argv) != 4:
    print "Correct usage: python chatapp.py <server IP address>, <server port number>, <name>"
    exit()

server      = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address  = str(sys.argv[1])
Port        = int(sys.argv[2])
name        = str(sys.argv[3])
server.connect((IP_address, Port))
server.send(name + " JOINED THE CHAT!")


while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print message
        else:
            message = sys.stdin.readline()
            server.send("[%s]\t%s\t"%(name, message))
            sys.stdout.write("[You]\t\t%s" % message)
            sys.stdout.flush()
server.close()
