#!/usr/bin/env python

import socket

ip = '192.168.1.168'
port = 5000
buffer = 8

user_outp = int(input("Which output? ")) - 1
user_inp = int(input("Which input? ")) - 1

#Outputs 1-4 use 00-03. Ouputs 5-8 use 11-14.
if user_outp > 3:
    user_outp = user_outp + 7

user_outp = str(user_outp)
user_inp = str(user_inp)
    
if len(user_inp) == 1:
    user_inp = '0' + user_inp

if len(user_outp) == 1:
    user_outp = '0' + user_outp

commandstring = '@T' + user_outp + user_inp + '#'
commandstring = commandstring.encode()

packet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
packet.connect((ip, port))
packet.send(commandstring)
data = packet.recv(buffer)
packet.close()
 
print("received data:", data)
