#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: main.py
@time: 2017/10/17 11:26
'''
#装饰器,函数与装饰器建立关系的方法:@装饰器
#@outer = outer(fun1),fun1函数没有()的情况下是导入函数，fun1函数添加()的情况下是执行函数。
#执行了包装了原函数(fun1)之后的新函数wrapper()。
#fun1 =
'''
    def wrapper():
        print '验证'
        fun()
        print '测试'
'''
'''
def outer(fun):
    def wrapper():
        print '验证'
        fun()
        print '测试'
    return wrapper()

@outer
def fun1():
    print 'fun1'

fun1
'''

'''
@outer
def fun2():
    print 'fun2'

@outer
def fun3():
    print 'fun3'
'''

#带参数的装饰器
'''
def outer(fun):
    def wapper(arg):
        print '带参数'
        fun(arg)
        print '完成带参数'
    return wapper

@outer
def fun1(arg):
    print 'fun1',arg

fun1('abc')
'''

#带返回值的装饰器
def outer(fun):
    def wapper(arg):
        print '带参数'
        result = fun(arg)
        return result
        print '完成带参数'
    return wapper


@outer
def fun1(arg):
    print 'fun1',arg
    return 'return'

respone = fun1('abc')
print respone