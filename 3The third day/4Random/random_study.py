#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: random_study.py
@time: 2017/10/13 15:06
'''
import random

'''
#随机生成一个数,在0-1数字区间
print random.random
#随机生成1-5范围内的整数，>=1 <=5
print random.randint(1,5)
#随机生成1-3范围内的参数，>=1 <3
print random.randrange(1,3)
'''

for i in range(6):
    if i == random.randint(1,100):
        print random.randint(1,100)
    else:
        temp = random.randint(65,90)
        print chr(temp)

#生成随机的六位英文字母终极版本
'''
code = []
for i in range(6):
    if i == random.randint(1,5):
        code.append(str(random.randint(1,5)))
    else:
        temp = random.randint(65,90)
        code.append(chr(temp))
print ''.join(code)
'''
