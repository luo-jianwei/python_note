#!/usr/bin/env python
# coding: UTF-8

import paramiko
import os
import sys

host = sys.argv[1]
user = 'root'
passwd = 'jianwei.com'

cmd = sys.argv[2]

# ��ʵ��
s = paramiko.SSHClient()
# ���ر���HOST�����ļ�
s.load_system_host_keys()
# ��һ������Ĭ�Ͻ�����Կ
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ����Զ������
s.connect(host,22,user,passwd,timeout=5)
# ִ������
stdin,stdout,stderr = s.exec_command(cmd)
# ��ȡ������
cmd_result = stdout.read(),stderr.read()

for line in cmd_result:
    print line
    
s.close()