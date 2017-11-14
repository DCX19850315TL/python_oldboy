#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: server1.py
@time: 2017/10/23 17:17
'''
import socket

sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,address = sk.accept()
    conn.send('hello.')
    flag = True
    while flag:
        data = conn.recv(1024)
        print data
        if data == 'exit':
            flag = False
        conn.send('sb')
    conn.close()