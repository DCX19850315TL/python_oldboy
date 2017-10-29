#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: demo.py
@time: 2017/10/25 17:42
'''
#生产者和消费者模型
#线程安全：队列，先进先出
#线程栈：后进先出
'''
from threading import Thread
from Queue import Queue

class Procuder(Thread):

    def run(self):
        Thread.run(self)

class Consumer(Thread):

    def run(self):
        Thread.run(self)

que = Queue(maxsize=100)  #队列限制为100
que.put('1')    #上传
que.put('2')
print que.qsize()   #获取上传数据的总数量
print que.get()     #下载
print que.get()
print que.empty()   #判断是否为空
'''
from threading import Thread
from Queue import Queue
import time

class Producer(Thread):

    def __init__(self,name,queue):
        self.Name = name
        self.Queue = queue
        super(Producer,self).__init__()

    def run(self):
        while True:
            if que.full():
                time.sleep(1)
            else:
                self.__Queue = que.put('baozi')
                time.sleep(1)
                print '%s 制作了一个包子'%(self.Name,)
        #Thread.run()

class Consumer(Thread):

    def __init__(self,name,queue):
        self.Name = name
        self.Queue = queue
        super(Consumer,self).__init__()

    def run(self):
        while True:
            if que.empty():
                time.sleep(1)
            else:
                self.__Queue = que.get()
                time.sleep(1)
                print '%s 消费了一个包子'%(self.Name,)
        #Thread.run()

que = Queue(maxsize=100)

tanglei1 =  Producer('唐磊1',que)
tanglei1.start()
tanglei2 =  Producer('唐磊2',que)
tanglei2.start()

for item in range(10):
    name = 'lihongwei%d' %(item,)
    temp = Consumer(name,que)
    temp.start()