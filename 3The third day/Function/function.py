#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: function.py
@time: 2017/9/28 16:02
'''
#函数特性：
#1.避免做重复的事情，将重复的事情封装成一个函数
#2.可以将多个功能分成多个函数
'''
def foo(name):
    print name,'学习'
foo('xixi')
foo('haha')
foo('hehe')
'''
'''
#函数练习
def login(username):
    if username == 'alex':
        return '登陆成功'
    else:
        return  '登陆失败'

def detail(user):
    print user,'XXXXXXXXXXXXXX'

def error():
    print '重试'

if __name__ == '__main__':
    user = raw_input('输入用户名:')

    res = login(user)
    if res == '登陆成功':
        print detail(user)
    else:
        print error()
'''

'''
#默认函数练习
def foo(name,action='学习',where='北京'):
    print name,'去',action,where

foo('a','砍柴')
foo('b','喝水')
foo('c')
foo('d',where='上海',action='hehe')
foo('e','上海','ee')
'''

#函数的可变参数
def show(*args):
    for item in args:
        print item

show('aa','bb','cc')    #将这些字符串变为列表传入到函数之中

def show2(**kargs):
    for item in kargs.items():
        print item
dict = {'a':1,'b':2}
show2(**dict)   #先定义字典，再将字典传入到函数之中
#show2(aa='111',bb='222')    #将这些字符串变为字典传入到函数之中


