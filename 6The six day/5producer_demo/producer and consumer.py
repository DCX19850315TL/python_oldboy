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
import random

def producer(name,que):
    while True:
        if que.qsize() < 3:
            que.put('baozi...')
            print '%s 生产了包子' %name
        else:
            print '还有三个包子'
        time.sleep(random.randrange(3))

def consumer(name,que):
    while True:
        try:
            que.get_nowait()
            print '%s 消费了包子' %name
        except Exception:
            print u'没有包子了'
        time.sleep(random.randrange(3))

q = Queue.Queue()

p1 = threading.Thread(target=producer,args=('tanglei1',q))
p2 = threading.Thread(target=producer,args=('tanglei2',q))
p1.start()
p2.start()


c1 = threading.Thread(target=consumer,args=('aa',q))
c2 = threading.Thread(target=consumer,args=('bb',q))
c1.start()
c2.start()