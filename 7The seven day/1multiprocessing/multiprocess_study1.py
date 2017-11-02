#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: multiprocess_study1.py
@time: 2017/10/30 16:12
'''
from multiprocessing import Pool
import time

def f(n):
    return n*n
    time.sleep(0.5)

if __name__ == '__main__':
    p = Pool(1)
    print (p.map(f,[1,2,3]))