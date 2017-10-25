#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: mythread.py
@time: 2017/10/25 17:09
'''
from threading import Thread
import time

class MyThread(Thread):

    def run(self):
        time.sleep(1)
        print '我是线程'

def Bar():
    print 'bar'

t1 = MyThread(target=Bar)
t1.start()
print 'over'

'''
class MyThread(Thread):

    def run(self):
        print 'myThread'
        Thread.run(self)

def Bar():
    print 'bar'

t1 = MyThread(target=Bar)
t1.start()
print 'over'
'''