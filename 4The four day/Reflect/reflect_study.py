#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: reflect_study.py
@time: 2017/10/16 12:18
'''
from web import account

#url以xxx/xxx的形式输入

'''
login = raw_input('输入:')
#array = account.split('/')
if login == 'account/login':
    account.login()
elif login == 'account/logout':
    account.logout()
'''

login = raw_input('输入:')
array = login.split('/')
model = __import__('web.'+array[0])
aa = getattr(model,array[0])
func = getattr(aa,array[1])
func()





