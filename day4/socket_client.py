#!/usr/bin/env python
# coding: UTF-8

import socket

host = '192.168.0.211'
port = 8999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

while True:
    user_input = raw_input('Please input something:').strip()
    if len(user_input) == 0:continue
    client.send(user_input)

    #判断返回数据的大小并接收返回值
    recv_size = client.recv(1024)
    recv_data = client.recv(int(recv_size) )
    print 'Receved:',recv_data
    
client.close()