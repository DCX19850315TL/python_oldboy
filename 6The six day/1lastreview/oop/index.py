#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2017/10/24 17:34
'''
class Foo(object):

    def __init__(self):
        print 'init'

    def __call__(self):
        return 'call'

foo = Foo()

foo()