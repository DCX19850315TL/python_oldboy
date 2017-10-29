#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: producer and consumer.py
@time: 2017/10/29 18:16
'''
#用函数的方式进行编写
import threading
import Queue
import time

def producer(name,que):

    que.put('baozi...')
    print '%s 生产了包子' %name

def consumer(name,que):

    que.get()
    print '%s 消费了包子' %name

q = Queue.Queue()

p1 = threading.Thread(targt=property,args=('tanglei1',q))
p2 = threading.Thread(targt=property,args=('tanglei2',q))

c1 = threading.Thread(targt=consumer,args=('aa',q))
c2 = threading.Thread(targt=consumer,args=('bb',q))