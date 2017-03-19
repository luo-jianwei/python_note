#!/usr/bin/env python
# coding: UTF-8

import socket

host = '192.168.0.211'
port = 8999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

while True:
    user_input = raw_input('Please input something:').strip()
    client.send(user_input)
    return_data = client.recv(1024)
    print 'Receved:',return_data
    
client.close()