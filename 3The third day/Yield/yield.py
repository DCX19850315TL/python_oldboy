#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: yield.py
@time: 2017/9/29 15:21
'''
#yield一般用在多线程的线程池,并且防止阻塞
'''
print range(10)
print xrange(10)
for item in xrange(10):
    print item
'''

#yield的原理介绍
'''
def foo():
    yield 1
re = foo()
print re
'''

'''
def aa():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for item in aa():
    print item
'''

#用with打开一个文件的方法
'''
with open('D:\\2Develop\\python_oldboy\\3The_third_day\\yield.txt','a') as f:
    f.write('\n5')
'''

#用yield模拟xreadline的过程
'''
def tangleixreadline():
    seek = 0
    while True:
        with open('D:\\2Develop\\python_oldboy\\3The_third_day\\tangleixreadline.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return

#print tangleixreadline()
for item in tangleixreadline():
    print item
'''

#三元运算法
'''
temp = None
if 1>3:
    temp = 'gt'
else:
    temp = 'lt'
print temp

result = 'gt' if 1>3 else 'lt'
print result
'''

#Lambda表达式，简单函数或者不经常用的函数可用lambda进行编写
'''
temp = lambda x,y:x+y
print temp(4,10)

#Lambda表达式的原始写法
def aa(x,y):
    return x+y
print aa(44,100)
'''
print([x*2 for x in range(10)])
print(map(lambda x:x*2, range(10)))
print(map(lambda x:x**x, range(10)))