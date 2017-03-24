#!/usr/bin/env python
# coding: UTF-8

import paramiko
import sys
import os

host = sys.argv[1]
cmd = sys.argv[2]
user = 'root'
port = 22
# ˽Կ·��
pkey_file = '/home/luojianwei/.ssh/id_rsa'

# ��ʵ��
s = paramiko.SSHClient()
# ���ر���HOST�����ļ�
s.load_system_host_keys()
# ��һ������Ĭ�Ͻ�����Կ
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ��Կ��֤
key = paramiko.RSAKey.from_private_key_file(pkey_file)
# ��������
s.connect(host,port,user,pkey=key,timeout=5)
# ִ������
stdin,stdout,stderr = s.exec_command(cmd)
# ��������ִ�н��
result = stdout.read(),stderr.read()

for line in result:
    print line

s.close()