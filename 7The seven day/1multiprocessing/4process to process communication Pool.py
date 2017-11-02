#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: 4process to process communication Pool.py
@time: 2017/10/31 10:27
'''
from multiprocessing import Pool
import time

def f(x):
    print x*x
    time.sleep(1)
    return x*x

pool = Pool(processes=4)
res_list = []

for i in range(10):
    res = pool.apply_async(f,[i,])

    print '---:',i
    res_list.append(res)

for r in res_list:
    print r.get()


#print pool.map(f,range(10)) #另外的一种写法