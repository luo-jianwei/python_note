#!/usr/bin/env python
# coding: UTF-8

import SocketServer

class MySockServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        print 'Got a new conn from ',self.client_address
        while True:
            data = self.request.recv(1024)
            print 'recv:',data
            self.request.send(data.upper())
        
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8999
    server = SocketServer.ThreadingTCPServer((host,port),MySockServer)
    
    server.serve_forever()
    
    