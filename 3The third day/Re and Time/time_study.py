#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: time_study.py
@time: 2017/10/15 15:24
'''
#三种形式
#时间戳格式
#元组格式
#格式化的字符串

import time
print time.time() #时间戳形式
print time.gmtime() #格式化的字符串
print time.strftime('%Y-%m-%d %H:%M:%S') #字符串格式化之后的时间

print time.strptime('2014-11-11' , '%Y-%m-%d') #字符串形式转换结构化形式
print time.localtime()
print time.mktime(time.localtime())#结构化的形式转换时间戳的形式