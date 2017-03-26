#!/usr/bin/env python
# coding: UTF-8
# description: python连接mysql程序,如果没有安装mysqldb模块,先运行sudo apt-wget install python-mysqldb安装

import MySQLdb

try:
    #实例化
    conn = MySQLdb.connect(host='192.168.0.199',user='root',passwd='python',db='zabbix',port=3306)
    #游标
    cur = conn.cursor()
    #执行语句
    cur.execute('show tables')
    #返回所有执行结果
    result = cur.fetchall()
    
    
    #打印结果
    for record in result:
        print record

    #切换database
    #conn.select_db('python')
    #返回前3条执行结果
    #result = cur.fetchmany(3)
    #写入操作需commit,commit后数据无法逆操作
    #cur.commit()
    
    cur.close()
    conn.close()
	
except MySQLdb.Error,e:
    print 'Mysql error message:',e 
