#!/usr/bin/env python
# coding: UTF-8

import paramiko
import os
import sys

host = sys.argv[1]
user = 'root'
passwd = 'jianwei.com'

cmd = sys.argv[2]

# 绑定实例
s = paramiko.SSHClient()
# 加载本机HOST主机文件
s.load_system_host_keys()
# 第一次连接默认接受密钥
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程主机
s.connect(host,22,user,passwd,timeout=5)
# 执行命令
stdin,stdout,stderr = s.exec_command(cmd)
# 读取命令结果
cmd_result = stdout.read(),stderr.read()

for line in cmd_result:
    print line
    
s.close()