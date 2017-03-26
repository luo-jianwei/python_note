#!/usr/bin/env python
# coding: UTF-8

import SocketServer
import commands
import time

class MySockServer(SocketServer.BaseRequestHandler):
    def recv_all(self,obj,msg_length,des_file):
        
        while msg_length != 0:
            if msg_length <= 4096:
                data = obj.recv(msg_length)
                msg_length = 0
            
            else:
                data = obj.recv(4096)
                msg_length -= 4096
            
            des_file.write(data)
            
        return 'Done'

    def handle(self):
        print 'Got a new conn from',self.client_address
        while True:
            cmd = self.request.recv(1024)
            if not cmd:
                print 'Lost connection with',self.client_address
                break
                
            option,filename,file_size = cmd.split()
            if option == 'put':
                #客户端上传文件
                f = file('recv/%s' %filename, 'wb')
                write_to_file = self.recv_all(self.request,int(file_size),f)
                if write_to_file == 'Done':
                    self.request.send('File upload success')
                    f.close()
            
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8999
    server = SocketServer.ThreadingTCPServer((host,port),MySockServer)
    
    server.serve_forever()