import socket 
import base64

# asking for the message using input()
message = input("Message? ")

# im gonna encode it into base 64 now so i dont have to worry about it later
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

# take the server name and port name 
host = 'YOUR IP HERE'
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
c.send(bytes(f"{base64_message}", encoding="ascii"))

c.close()

keep = input("Want to send another message? Y/N: ")
if keep == "N":
	c.close()
if keep == "Y":
	message = input("Message? ")

	# im gonna encode it into base 64 now so i dont have to worry about it later
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')

	host = 'local host'
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
	print("Found Reciever At:", str(addr)) 

	# send message to the client after 
	# encoding into binary string 
	c.send(bytes(f"{base64_message}", encoding="ascii"))

	c.close()

	
while keep == "Y":
	message = input("Message? ")

	# im gonna encode it into base 64 now so i dont have to worry about it later
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')

	host = 'local host'
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
	print("CONNECTION FROM:", str(addr)) 

	c.send(bytes(f"{base64_message}", encoding="ascii"))

	c.close()

	



# disconnect the server  
