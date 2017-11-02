#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: multiprocess_study1.py
@time: 2017/10/16 11:47
'''
str1 = 'demo'
str2 = 'foo'

module = __import__(str1)
func = getattr(module,str2)
func()