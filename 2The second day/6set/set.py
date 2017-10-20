#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#集合的演示

name_set = {1,2,3,4}
name_set.add(5) #增加一个值
print(name_set)
# name_set.pop()  #从第一个开始删除

#集合的关系测试
x = {1,2,3,4}
y = {3,4,5,6}
z = {1,2,4}
print (x & y)   #交集
print(x | y)    #和集
print(x - y)    #差集
print(x ^ y)    #对称差集
print(z.issubset(x))    #z是x的子集
print(x.issuperset(z))  #x是z的父集

