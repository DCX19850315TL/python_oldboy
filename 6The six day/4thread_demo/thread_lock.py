#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: thread_lock.py
@time: 2017/10/30 11:49
'''
import threading
import time
'''
num = 0

def run(n):

    #time.sleep(1)
    global num
    lock.acquire()
    num +=1
    lock.release()
    time.sleep(0.01)
    print '%s\n'%num

lock = threading.Lock()   #锁方法
#lock = threading.RLock()    #递归锁

for i in range(100):
    p1 = threading.Thread(target=run,args=(i,))
    p1.start()
'''
'''
num = 0

num2 = 0

def run(n):

    #time.sleep(1)
    global num,num2 #局部变量可以修改全局变量的方法,一般不推荐使用
    lock.acquire()
    num +=1
    lock.acquire()
    num2 +=1

    lock.release()
    lock.release()
    time.sleep(0.01)
    print '%s\n'%num

lock = threading.RLock()    #递归锁

for i in range(100):
    p1 = threading.Thread(target=run,args=(i,))
    p1.start()
'''
num = 0

num2 = 0

def run(n):

    #time.sleep(1)
    global num  #局部变量可以修改全局变量的方法,一般不推荐使用
    samp.acquire()
    time.sleep(0.001)
    num +=1
    print '%s' % num
    samp.release()
    #time.sleep(0.01)

samp = threading.BoundedSemaphore(4)    #信号量

for i in range(200):
    p1 = threading.Thread(target=run,args=(i,))
    p1.start()