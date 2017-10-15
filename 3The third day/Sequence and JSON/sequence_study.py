#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: sequence_study.py
@time: 2017/10/15 14:29
'''
#序列化:把一个对象（列表，字典）通过python特有的机制给序列化，就是以特殊二进制的方式加密，这个过程就叫序列化。对一个类，对象进行序列化之后也可以进行反序列化。
#把列表序列化成一个字符串的形式,并且是无规则的,python与python之间的传输，用序列化的方式。两个python程序之间进行数据的交互。
import pickle

li = ['alex',11,22,'ok','sb']
'''
dumpsed = pickle.dumps(li)
print dumpsed
loadsed = pickle.loads(dumpsed)
print loadsed
'''

#dumpsed = pickle.dump(li,open('D:\\2Develop\\python_oldboy\\3The_third_day\\sequence.txt','w'))
result = pickle.load(open('D:\\2Develop\\python_oldboy\\3The_third_day\\sequence.txt','r'))
print result



