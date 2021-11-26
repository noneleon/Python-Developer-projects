'''
Description
The admin noticed someone sneaking around the site with admin rights and came up with a password. Now to log in as an admin, you need to enter the password first. Maybe the admin has set a relatively easy and short password so that it is easy to remember? Let's try to brute force all possible passwords to enter the site!

So far the program is very simplistic: it’s time to improve it so that it can generate different variants of the password and then try each one. The admin of the server doesn’t hide the information that passwords vary in length and may include letters from a to z and numbers from 0 to 9. You should start with a,b,c,....,z,0,1,..aa,ab,ac,ad and continue until your password is correct. It’s very important to try all the variants of every length because otherwise your program risks never finding the password!

If the password is correct, you will receive the “Connection success!” message. Otherwise, you will see the “Wrong password!” message. The server cannot receive more than a million attempts, so if your program works indefinitely, you will see the unfortunate message “Too many attempts”.

Objectives
In this stage, you should write a program that:

Parses the command line and gets two arguments that are IP address and port.
Tries different passwords until it finds the correct one.
Prints the password it found.
Note that you can connect to the server only once and then send messages many times. Don't connect to the server before sending every message.

Also, note that here and throughout the project, the password is different every time you check your code.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

> python hack.py localhost 9090
pass
'''
import itertools
import socket
import string
import sys


symbols = string.ascii_lowercase + string.digits


def generate_password():
    for length in range(1, len(symbols) + 1):
        for item in itertools.product(symbols, repeat=length):
            yield ''.join(item)


args = sys.argv
with socket.socket() as client_socket:
    client_socket.connect((args[1], int(args[2])))
    poss_values = generate_password()
    for attempt in poss_values:
        password = ''.join(attempt)
        client_socket.send(password.encode())
        response = client_socket.recv(1024)
        if response.decode() == 'Connection success!':
            print(password)
            exit()
 \\

import socket,sys,string,itertools


admin_hn = sys.argv[1]
admin_p = int(sys.argv[2])
chr_set = string.ascii_lowercase + string.digits


def generate_password():
    for length in range(1, len(chr_set) + 1):
        for product in itertools.product(chr_set, repeat=length):
            yield ''.join(product)


with socket.socket() as admin_socket:
    admin_socket.connect((admin_hn, admin_p))
    for password in generate_password():
        admin_socket.send(password.encode())
        response = admin_socket.recv(1024).decode()
        if response == 'Connection success!':
            print(password)
            break
