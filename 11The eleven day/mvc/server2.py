#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: server2.py
@time: 2017/11/14 22:09
'''
#controller模块:业务逻辑处理
#model模块:对数据库操作
#view模块:放html文件
from wsgiref.simple_server import make_server

def index():
    return index

def login():
    #1.打开html文件
    #2.读取html文件中的内容
    #html = '''<p>Username:<input ></p><p>Password:<input></p>'''
    #return html
    return login

url = (
    ('/index/',index),
    ('/login/',login),
)

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #1.获取用户的URL
    userUrl = environ['PATH_INFO']

    func = None

    for item in url:
        if item[0] == userUrl:
            return item[1]()
            #func = item[1]
            #break
    '''
    if func:
        result = func()
    else:
        result = '404'
    return result
    '''
    '''
        #2.根据URL的不同访问不同的页面
        if userUrl == '/login':
            return '<h1>login</h1>'
        elif userUrl == '/logout':
            return '<h1>logout</h1>'
        else:
            return '<h1>404 not found</h1>'
        '''
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()