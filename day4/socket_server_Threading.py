#!/usr/bin/env python
# coding: UTF-8

import SocketServer
import commands
import time

class MySockServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        print 'Got a new conn from ',self.client_address
        while True:
            cmd = self.request.recv(1024)
            if not cmd:
                print 'Host connection with',self.client_address
                break
            #print 'recv:',
            #self.request.send(data.upper())
            #接收客户端发送的命令
            cmd_result = commands.getstatusoutput(cmd)
            #返回命令结果的长度
            self.request.send(str(len(cmd_result[1])))
            #解决粘包问题
            time.sleep(0.2)
            #返回命令执行结果
            self.request.sendall(cmd_result[1])
            
            print 'recv:',cmd_result[1]
            
                    
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8999
    server = SocketServer.ThreadingTCPServer((host,port),MySockServer)
    
    server.serve_forever()
    
    