import tkinter as tk
from tkinter import ttk
import socket
import base64
import codecs


window = tk.Tk()
window.title("CarbonMessages ALPHA")
window.minsize(400,200)

ROT13bool = tk.IntVar()
chkbox = tk.Checkbutton(text="Use ROT13?", variable=ROT13bool)
chkbox.pack()

def clickMe():
	if (ROT13bool.get()) == 0:
		message_bytes = name.get().encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		base64_message = base64_bytes.decode('ascii')
	else:
		rot13_bytes = codecs.encode(f'{name.get()}', 'rot_13')

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

	if (ROT13bool.get()) == 0:
		c.send(bytes(f"{base64_message}", encoding="ascii"))
	else:
		c.send(bytes(f"{rot13_bytes}", encoding="ascii"))

	c.close()



label = tk.Label(window, text = "Enter Your message")
label.pack()





name = tk.StringVar()
messageEntered = ttk.Entry(window, width = 15, textvariable = name)
messageEntered.pack()


button = ttk.Button(window, text = "Send", command = clickMe)
button.pack()


MyTitle2 = tk.Label(window, text="CURRENTLY IN BETA", font="Hevetica 12 bold", fg='black', bg='white')
MyTitle2.pack()

window.mainloop()
