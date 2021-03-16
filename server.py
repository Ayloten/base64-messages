import socket 
import base64
import codecs

# rot 13 time
rot13bool = input("would you like to use ROT13? Y for Yes, N for no.")

# asking for the message using input()
message = input("Message? ")

# im gonna encode it into base 64 now so i dont have to worry about it later
if rot13bool == 'N':
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
else:
	rot13_bytes = codecs.encode(f'{message}', 'rot_13')

# take the server name and port name 
host = ''
port = 5000

# create a socket at server side 
# using TCP / IP protocol 
s = socket.socket(socket.AF_INET, 
				socket.SOCK_STREAM) 

# bind the socket with server 
# and port number 
s.bind(('', port)) 

# allow maximum 1 connection to 
# the socket 
s.listen(1) 

# wait till a client accept 
# connection 
c, addr = s.accept() 

# send message to the client after 
# encoding into binary string
if rot13bool == "N": 
	c.send(bytes(f"{base64_message}", encoding="ascii"))
else:
	c.send(bytes(f"{rot13_bytes}", encoding="ascii"))

c.close()

keep = input("Want to send another message? Y/N: ")
if keep == "N":
	c.close()
if keep == "Y":
	rot13bool = input("would you like to use ROT13? Y for Yes, N for no.")

# asking for the message using input()
	message = input("Message? ")

# im gonna encode it into base 64 now so i dont have to worry about it later
	if rot13bool == 'N':
		message_bytes = message.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		base64_message = base64_bytes.decode('ascii')
	else:
		rot13_bytes = codecs.encode(f'{message}', 'rot_13')

	host = ''
	port = 5000

	# create a socket at server side 
	# using TCP / IP protocol 
	s = socket.socket(socket.AF_INET, 
				socket.SOCK_STREAM) 

	# bind the socket with server 
	# and port number 
	s.bind(('', port)) 

	# allow maximum 1 connection to 
	# the socket 
	s.listen(1) 

	# wait till a client accept 
	# connection 
	c, addr = s.accept() 

	# display client address
	if addr != host: 
		print("Found Reciever At:", str(addr))
	else:
		print("self connected.") 

	if rot13bool == "N": 
		c.send(bytes(f"{base64_message}", encoding="ascii"))
	else:
		c.send(bytes(f"{rot13_bytes}", encoding="ascii"))

	c.close()

	
while keep == "Y":
	rot13bool = input("would you like to use ROT13? Y for Yes, N for no.")

	# asking for the message using input()
	message = input("Message? ")

	# im gonna encode it into base 64 now so i dont have to worry about it later
	if rot13bool == 'N':
		message_bytes = message.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		base64_message = base64_bytes.decode('ascii')
	else:
		rot13_bytes = codecs.encode(f'{message}', 'rot_13')

	host = ''
	port = 5000

	# create a socket at server side 
	# using TCP / IP protocol 
	s = socket.socket(socket.AF_INET, 
				socket.SOCK_STREAM) 

	# bind the socket with server 
	# and port number 
	s.bind(('', port)) 

	# allow maximum 1 connection to 
	# the socket 
	s.listen(1) 

	# Wanit till a client accept 
	# connection 
	c, addr = s.accept() 

	# display client address 
	if addr != host:
		print("CONNECTION FROM: ", str(addr)) 
	else:
		print("self connected")

	if rot13bool == "N": 
		c.send(bytes(f"{base64_message}", encoding="ascii"))
	else:
		c.send(bytes(f"{rot13_bytes}", encoding="ascii"))

	c.close()

	



# disconnect the server  
