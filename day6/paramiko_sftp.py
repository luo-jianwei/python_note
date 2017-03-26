#!/usr/bin/env python
# coding: UTF-8

import os
import sys
import paramiko

host = '192.168.0.199'
user = 'root'
password = 'jianwei.com'

t = paramiko.Transport((host,22))
# 密码认证
# t.connect(username=user,password=password)

# 密钥认证
pkey_file = '/home/luojianwei/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)
t.connect(username=user,pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)

# 下载远程主机aaaa文件到本地
sftp.get('/tmp/aaaa','aaaa')
# 上传本地文件bbbb到远程主机
sftp.put('bbbb','/tmp/bbbb')

t.close()