#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: conf.py
@time: 2017/11/15 14:34
'''
#使用配置文件进行url和内容的映射关系
def index():
    return index

def login():
    #1.打开html文件
    #2.读取html文件中的内容
    html = '''<p>Username:<input ></p><p>Password:<input></p>'''
    return html

url = (
    ('/index',index),
    ('/login',login),
)

print(login())