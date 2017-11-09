
#!/usr/bin/env python
import socket
import re


def template(id):
    return """HTTP/1.0 200 OK
            Content-Type: text/html



            <!DOCTYPE html>
              <head>
                <title>Success</title>
                   </head>
                   <body>
                    Successfully receieved the data!!
                    Provided id is  \"""" + id + """\"
                    </body>
                </html>
            """


# ##############################################################


def main():
    # Standard socket stuff:
    host = 'localhost'  # do we need socket.gethostname() ?
    port = 8085
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)  # don't queue up any requests

    # Loop forever, listening for requests:
    while True:
        print "Waiting....."
        csock, caddr = sock.accept()
        print "Connection from: " + `caddr`
        req = csock.recv(1024)  # get the request, 1kB max
        print req
        match = re.match('GET /\?id=([-\.\w\d]+)\sHTTP/1', req)
        if match:
            angle = match.group(1)
            print "id =: " + angle + ""
            op = template(angle)
            csock.sendall(op)
            csock.close()
        else:
            print "Returning 404"
            csock.sendall("HTTP/1.0 404 Not Found\r\n\n 404 Page Not Found!")
            csock.close()


if __name__ == '__main__':
    main()
