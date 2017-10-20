#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: setter.py
@time: 2017/10/18 15:59
'''
#第四天21课
class test1:

    def __init__(self):
        self.__pravite = 'alex'

    @property
    def show(self):
        return self.__pravite

class test2:

    def __init__(self):
        self.__pravite = 'alex2'

    @property
    def show(self):
        return self.__pravite

    @show.setter
    def show(self,value):
        self.__pravite = value

t1 = test1()
print t1.show
t1.show = 'change1'
print t1.show

t2 = test2()
print t2.show
t2.show = 'chanage3'
print t2.show