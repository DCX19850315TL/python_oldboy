#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2017/10/25 12:20
'''
#1.计算密集型的程序在Python中运用多进程的方式
#2.IO密集型的程序在Python中运用多线程的方式
#Python与其它语言的区别在于有全局解释器的存在，导致每个进程中只能有一个线程进行计算，为了可以提高计算效率，发明了多进程。但是由于进程与进程间的信息无法共享，所以Python在使用多进程的时候会占用更多的内存。