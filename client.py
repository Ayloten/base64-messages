import socket 
import base64
import sys
import contextlib

sys.tracebacklimit = 1

# take the server name and port name.
host = 'YOUR IP HERE'
port = 5000

# create a socket at client side 
# using TCP / IP protocol 
s = socket.socket(socket.AF_INET, 
				socket.SOCK_STREAM) 

# connect it to server and port 
# number on local computer.
with contextlib.suppress(ConnectionRefusedError):
	s.connect(('YOUR IP HERE', port)) 

# receive message string from 
# server, at a time 1024 B
with contextlib.suppress(OSError):
	msg = s.recv(1024)

# repeat as long as message 
# string are not empty
with contextlib.suppress(NameError): 
	while msg:
		recievedmsg = msg.decode()
		msg = s.recv(1024)

# decoding base64
with contextlib.suppress(NameError):
	p = recievedmsg
	d = base64.b64decode(p)
	f = d.decode("utf-8")
	print(f)

# disconnect the client a 
s.close()
