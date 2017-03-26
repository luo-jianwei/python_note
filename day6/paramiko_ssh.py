#!/usr/bin/env python
# coding: UTF-8

import paramiko
import sys
import os

host = sys.argv[1]
cmd = sys.argv[2]
user = 'root'
port = 22
# 私钥路径
pkey_file = '/home/luojianwei/.ssh/id_rsa'

# 绑定实例
s = paramiko.SSHClient()
# 加载本机HOST主机文件
s.load_system_host_keys()
# 第一次连接默认接受密钥
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 密钥认证
key = paramiko.RSAKey.from_private_key_file(pkey_file)
# 连接主机
s.connect(host,port,user,pkey=key,timeout=5)
# 执行命令
stdin,stdout,stderr = s.exec_command(cmd)
# 返回命令执行结果
result = stdout.read(),stderr.read()

for line in result:
    print line

s.close()