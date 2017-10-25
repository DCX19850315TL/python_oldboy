#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: demo.py
@time: 2017/10/25 17:42
'''
from threading import Thread

class Procuder(Thread):

    def run(self):
        Thread.run(self)

class Consumer(Thread):

    def run(self):
        Thread.run(self)



