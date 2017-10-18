#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: setter.py
@time: 2017/10/18 15:59
'''
from web import account

login = raw_input('输入:')
array = login.split('/')
model = __import__('web.'+array[0])
aa = getattr(model,array[0])
func = getattr(aa,array[1])
func()