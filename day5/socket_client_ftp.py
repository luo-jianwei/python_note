#!/usr/bin/env python
# coding: UTF-8

import socket
import os

host = '192.168.0.211'
port = 8999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

while True:
    user_input = raw_input('Please input something:').strip()
    if len(user_input) == 0:continue
    
    #把字符转换为列表
    user_cmd = user_input.split()
    if user_cmd[0] == 'put':
        if len(user_cmd) == 2:
            f = file(user_cmd[1],'rb')
            f_size = os.stat(user_cmd[1]).st_size
            client.send("%s %s %s" %(user_cmd[0],user_cmd[1],f_size))
            
            print 'going to send...'
            client.sendall(f.read())
            print client.recv(1024)
            
#    recv_size = client.recv(1024)
#    recv_data = client.recv(int(recv_size) )
#    print 'Receved:',recv_data
    
client.close()