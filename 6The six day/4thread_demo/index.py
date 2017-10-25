#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2017/10/25 14:37
'''
from threading import Thread
import time
'''
def Foo(arg,v):
    print arg

print 'before'
t1 = Thread(target=Foo,args=('aaaaa',11,))   #创建线程
t1.start()
print t1.getName()
print 'after'

t2 = Thread(target=Foo,args=('aaaaa',11,))   #创建线程
t2.start()
print t2.getName()
print 'after'
'''
def Foo(arg,v):
    for item in range(100):
        print item
        time.sleep(1)

print 'before'
t1 = Thread(target=Foo,args=('aaaaa',11,))   #创建线程
t1.setDaemon(True)
t1.start()
t1.join()   #到join的停掉主线程，执行子线程，直到子线程执行完毕后，在执行主线程。其中如果添加参数5，说明到join的时候会执行主线程，但只执行5秒，又会回到执行子线程。

print 'after'
print 'after'
print 'after'
print 'after end'
time.sleep(10)