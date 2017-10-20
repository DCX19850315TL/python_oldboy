#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2017/10/12 22:40
'''

temp = 'mysqlconnect'
model = __import__(temp)
model.count


'''
temp = 'mysqlconnect'
func = 'count'
model = __import__(temp)
1function = getattr(model,func)
print 1function()
'''