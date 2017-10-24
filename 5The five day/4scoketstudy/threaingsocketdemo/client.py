#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: client.py
@time: 2017/10/23 17:17
'''
import socket

client = socket.socket()

ip_port = ('127.0.0.1',9999)

client.connect(ip_port)

while True:
    data = client.recv(1024)
    print data
    inp = raw_input('clent:')
    client.send(inp)
    if inp == 'exit':
        break
