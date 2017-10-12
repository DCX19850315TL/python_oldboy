#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: built-in function.py
@time: 2017/10/10 16:35
'''
#内置函数
'''
help()
dir()   #显示当前的key
vars()  #显示当前的key-value
type()  #查看变量什么类型
import temp #导入模块
reload(temp)    #重新导入模块
id()    #查看对应的变量内存地址
'''

'''
print abs(-9)   #绝对值
print bool(0)   #布尔值
print divmod(9,3)   #求9除以3的值和余数，用于网页分页的场景
print max([1,2,3])  #取最大值
print min([1,2,3])  #取最小值
print sum([1,2,3])  #求和
print pow(2,10)     #求指数
'''

'''
print all([1,2,3,0])    #如果列表中有一个为0则为False
print any([0,0,0,0])    #如果列表中全部都为0则为False
print any([1,0,0,0])    #如果列表中有一个为1则为True，可以通过此方法判断字符串中是否有空字符串
'''

'''
print chr(65)   #ASCII转换
print ord('A')

print hex(2000)     #十六进制
print oct(2000)     #八进制
print bin(2)        #二进制
'''

'''
#给列表中的字符串增加编号
list = ['汽车','房子','手机']
for item in list:
    print item

for temp in enumerate(list,1):
    print temp[0],temp[1]
'''

'''
#使用变量的另外一种形式,类似%s
s = 'i am is {0},{1}'
print s.format('tanglei','lihongwei')
'''

'''
#未使用map前的复杂代码
li = [11,22,33]

temp = []

for item in li:
    temp.append(item + 100)

print temp
#使用map的代码,对所有的元素做操作
def foo(arg):
    return arg + 100
temp = map(foo,li)
print temp
#使用map+lambda的代码，遍历li列表中的数据，将数据转换为参数，赋予到函数中
temp = map(lambda arg:arg+100,li)
print temp
'''

#过滤
'''
list = [11,22,33]
def foo(arg):
    if arg < 23:
        return True
    else:
        return False
temp = filter(foo,list)
print temp
'''

#累加,累乘
'''
list = [1,2,3,4,5]
temp = reduce(lambda x,y:x+y,list)
print temp
'''

#zip,把多个列表的同一列重新生成一个列表
'''
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
temp = zip(a,b,c)
print temp
'''

#对字符串进行运算
'''
a = '8 * 8'
print eval(a)
'''

#反射:通过字符串的形式导入模块,并以字符串的形式执行函数
#开发大型程序,涉及切换数据库
#设计模式,工厂模式,
'''
temp = 'sys'
model = __import__(temp)
print(model.path)
'''
