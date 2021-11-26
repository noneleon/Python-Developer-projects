'''
Description
Imagine some admin who runs a website on the Internet. The site is becoming very popular, and a lot of people register. Filling in their profiles, they leave some information there that is not meant to be public, for example, information about their credit cards.

The admin completely forgot about the security of the site, so now you can log in with admin privileges without even having a login and password!

The first task of this project is to go to the admin's site; it will immediately give out all the secret information. Remember, as soon as you enter the site as an admin, you will automatically obtain all the private data of the site. It will get harder: the tasks of all other stages of the project will be to crack the admin password. Good luck!

Your program should connect to the server using an IP address and a port from the command line arguments. You can use socket module to create this program.

Objectives
Your program will receive command line arguments in this order:

IP address
port
message for sending
The algorithm is the following:

Create a new socket.
Connect to a host and a port using the socket.
Send a message from the third command line argument to the host using the socket.
Receive the server’s response.
Print the server’s response.
Close the socket.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> python hack.py localhost 9090 password
Wrong password!
Example 2:

> python hack.py 127.0.0.1 9090 qwerty
Connection Success!
'''

# write your code here
import sys
import socket


ip, port, message = sys.argv[1:]
with socket.socket() as client_socket:
    client_socket.connect((ip, int(port)))
    client_socket.send(message.encode())
    print(client_socket.recv(1024).decode())
    
\\

import sys
import socket

new_sock = socket.socket()
address, port, word = sys.argv[1:]

new_sock.connect((address, int(port)))
message = word.encode()
new_sock.send(message)

a = new_sock.recv(1024)
print(a.decode())