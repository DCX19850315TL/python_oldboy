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
#print tanglei.Name,tanglei.Age

class car:

    def __init__(self,country,brand,model):
        self.Country = country
        self.Brand = brand
        self.Model = model

BMW = car('德国','宝马','SUV')
AUDI = car('德国','奥迪','B级轿车')
#print BMW.Country,BMW.Brand,BMW.Model
#print AUDI.Country,AUDI.Brand,AUDI.Model

class Province(object):     #继承object
    # 属于类的字段如:memo = 叫做静态字段，使用self.的字段叫做动态字段
    memo = '中国２３个省之一'   #属于类

    def __init__(self,name,capital,leader,flag):
        self.Name = name
        self.Capital = capital
        self.Leader = leader
        self.__China = flag     #私有字段

    #动态方法
    def sports_meet(self):
        print self.Name + '正在开运动会'

    #静态方法,去掉self（对象）
    @staticmethod
    def Foo():
        print '每个省都带头反腐'

    #特性
    @property
    def Bar(self):
        print self.Name
        return '特性'

    #私有字段:用在别人不能改，但可以进行访问
    def show(self):
        print self.__China

    @property       #通过属性可以直接定义私有字段，且是只读
    def China(self):
        return self.__China

    #私有字段可写
    @China.setter
    def China(self,value):
        self.__China = value

    #私有方法
    def __sha(self):
        print '我是alax'

    def foo2(self):
        self.__sha()

#hb和sd属于对象，self.Name等属于这个对象的方法
#在类里面定义方法，让对象使用
#hb = Province('河北','石家庄','李扬')
#sd = Province('山东','济南','王胜辉')
japan = Province('日本','济南','王胜辉',True)

#print hb.Name
#print Province.memo
#print japan.__China    #外部无法直接调用内部字段
#japan.show()    #通过定一个方法来调用内部字段
#print japan.China   #通过属性可以直接调用内部字段
#japan.__sha()   #外部无法直接调用内部方法
#japan.foo2()    #通过定义一个共有方法foo2来调用内部方法
#japan._Province__sha()  #不用定义共有方法直接调用私有方法的写法
'''
#推荐访问私有字段的方法
print japan.China
japan.China = False
print japan.China
'''
#静态类不能访问动态字段
#print Province.Name
#对象可以访问静态字段,但尽量不要使用
#print hb.memo

#对象可以访问动态方法
#类不许使用动态方法，因为没有实例化
#hb.sports_meet()

#类使用静态方法
#Province.Foo()
#对象使用静态方法
#hb.Foo()

#特性:把方法的访问形式变成字段的访问形式，可以使用返回值
#hb.Bar
#print hb.Bar

#模块化编程和面向对象编程
#反射加上模块化编程能100%模拟面向对象编程
#JAVA，C#都是面向对象的编程方式，而python即支持面向对象编程也支持模块化编程

#在销毁对象的时候,要做的动作写到析构函数
'''
class Foo:

    def __init__(self):
        pass

    def __del__(self):  #一般情况下永不到，永远是最后执行的
        print '解释器要销毁前,可以做的事情'

    def GO(self):
        print 'GO'

    def __call__(self):
        print 'call'

f1 = Foo()  #执行init方法
f1.GO()
f1()    #执行类的__call__方法
'''

#类的继承
#父类，子类或者叫基类，派生类
#有object的叫做新式类，没有object的叫做经典类
#新式类比经典类提供的内容多一些
class father(object):

    def __init__(self):
        self.Name = 'fff'
        print 'father __init__'

    def Fa(self):
        print 'father'

    def Bad(self):
        print '抽烟'

class son(father):

    def __init__(self):
        self.Name = 'sss'
        print 'son __init__'
        father.__init__(self)   #在子类执行父类的构造函数
        super(son,self).__init__()  #在子类执行父类的构造函数的另一种方法

    def sonn(self):
        print 'son'
    '''
    def Bad(self):
        print '抽烟戒掉了'
    '''
    def Bad(self):
        father.Bad(self)
        print '抽烟戒掉了'

son1 = father()
son1.Fa()   #父类对象的方法
son2 = son()
son2.sonn() #子类对象的方法
son2.Fa()   #子类继承父类对象的方法
son2.Bad()  #子类继承父类方法后，子类的对象方法将父类的方法修改掉

#类的多继承
class A(object):    #新式类解决掉经典类的BUG
    def __init__(self):
        print 'This is A'
    def save(self):
        print 'save method from A'

class B(A):
    def __init__(self):
        print 'This is B'

class C(A):
    def __init__(self):
        print 'This is C'
    def save(self):
        print 'save method from --C--'

class D(B,C):
    def __init__(self):
        print 'This is D'

c = D()
c.save()

#抽象类
#抽象类+抽象方法 = 接口(第二种接口，即：规范)
from abc import ABCMeta,abstractmethod

class Alert:
    __metaclass__ = ABCMeta

    @abstractmethod
    def Send(self):pass

class Weixin(Alert):
    def __init__(self):
        print '__init__'

    def Send(self):
        print 'send.Weixin'

f = Weixin()
f.Send()