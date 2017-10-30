#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: multi1.py
@time: 2017/10/30 17:49
'''
#from multiprocessing import Process,Queue
from multiprocessing import Process,Queue

def f(q,n):
    q.put([n,'hello'])

if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        p = Process(target=f,args=(q,i))
        p.start()
    print q.get()

