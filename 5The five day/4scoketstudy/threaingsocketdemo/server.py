#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: server1.py
@time: 2017/10/24 10:24
'''
import SocketServer

class MyServer(SocketServer.BaseRequestHandler):

    def setup(self):
        pass

    def handle(self):
        conn = self.request
        conn.send('hello.')
        flag = True
        while flag:
            data = conn.recv(1024)
            print data
            if data == 'exit':
                flag = False
            conn.send('sb')
        conn.close()

    def finish(self):
        pass

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()
