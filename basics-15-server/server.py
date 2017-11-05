#!/usr/bin/env python
import socket
import re

def head():
	return """HTTP/1.0 200 OK
		Content-Type: text/html

		"""

def template():
	return 	"""
		<!DOCTYPE html>
 		   <head>
			<title>Success</title>
		   </head>
		   <body>
			Successfully receieved the data!!
			Provided id is  \"""" + angle + """\"
		   </body>
		</html>
		"""

def fb_json(fb_id):
	pass

# ##############################################################

if __name__ == '__main__':
	# Standard socket stuff:
	host = 'localhost' # do we need socket.gethostname() ?
	port = 8085
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(1) # don't queue up any requests

	# Loop forever, listening for requests:
	while True:
		csock, caddr = sock.accept()
		print "Connection from: " + `caddr`
		req = csock.recv(1024) # get the request, 1kB max
		print req
	    # Look in the first line of the request for a move command
	    # A move command should be e.g. 'http://server/move?a=90'
		match = re.match('GET /\?id=([\w]+)\sHTTP/1', req)
		if match:
			id_from_url = match.group(1)
			csock.sendall(head()+template())
			csock.close()
		else:
			print "Returning 404"
			csock.sendall("HTTP/1.0 404 Not Found\r\n\n <h1>404 Page Not Found!</h1>")
			csock.close()
