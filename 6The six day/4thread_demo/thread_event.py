#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: thread_event.py
@time: 2017/10/30 14:31
'''
import threading
import time

def producer():

    event.wait()
    event.clear()
    print '厨师:等着人来买包子'

    print '厨师:包子正在制作之中。。。'
    time.sleep(3)

    event.set()
    print '厨师:包子做好了'

def consumer():

    event.set()
    print '唐磊:去买包子'

    time.sleep(1)
    print '唐磊:在等待厨师做包子'

    while True:
        if event.isSet():
            print '唐磊:谢谢，包子很好吃'
            break
        else:
            print '唐磊:有点慢'
    #event.wait()

    #print '唐磊:谢谢，包子很好吃'

event = threading.Event()
p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()