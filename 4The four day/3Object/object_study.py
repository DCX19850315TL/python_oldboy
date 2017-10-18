#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: object_study.py
@time: 2017/10/17 14:30
'''
#面向对象的一个关键点:创建对象的动作叫做实例化
#类:创建类的目的是对某一类别的东西进行抽象
#方法，特性，字段目的：提供统一的方法或者数据，处理这一类的请求

class person:

    def __init__(self,name,age):
        self.Name = name
        self.Age = age

tanglei = person('唐磊',30)
print tanglei.Name,tanglei.Age

class car:

    def __init__(self,country,brand,model):
        self.Country = country
        self.Brand = brand
        self.Model = model

BMW = car('德国','宝马','SUV')
AUDI = car('德国','奥迪','B级轿车')
print BMW.Country,BMW.Brand,BMW.Model
print AUDI.Country,AUDI.Brand,AUDI.Model

class Province:
    # 属于类的字段如:memo = 叫做静态字段，使用self.的字段叫做动态字段
    memo = '中国２３个省之一'   #属于类

    def __init__(self,name,capital,leader):
        self.Name = name
        self.Capital = capital
        self.Leader = leader

    #动态方法
    def sports_meet(self):
        print self.Name + '正在开运动会'

    #静态方法,去掉self（对象）
    @staticmethod
    def Foo():
        print '每个省都带头反腐'

    #方法变为特性
    @property
    def Bar(self):
        print self.Name
        return '特性'

#hb和sd属于对象，self.Name等属于这个对象的方法
#在类里面定义方法，让对象使用
hb = Province('河北','石家庄','李扬')
sd = Province('山东','济南','王胜辉')

print hb.Name
print Province.memo

#静态类不能访问动态字段
#print Province.Name
#对象可以访问静态字段,但尽量不要使用
print hb.memo

#对象可以访问动态方法
#类不许使用动态方法，因为没有实例化
hb.sports_meet()

#类使用静态方法
Province.Foo()
#对象使用静态方法
hb.Foo()

#特性:把方法的访问形式变成字段的访问形式，可以使用返回值
hb.Bar
print hb.Bar



