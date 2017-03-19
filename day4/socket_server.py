#!/usr/bin/env python
# coding: UTF-8

import socket

host = '0.0.0.0'
port = 8999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)

while True:
    conn,addr = server.accept()
    print 'Got a connection from:',addr
    
    while True:
        data = conn.recv(1024)
        if not data:break
        conn.send(data.upper())
        print 'Received:',data
        
server.close()

