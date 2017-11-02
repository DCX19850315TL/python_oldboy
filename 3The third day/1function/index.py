#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: multiprocess_study1.py
@time: 2017/9/28 15:31
'''
from file import demo
#demo.foo() #引用自己创建的package中的foo函数
print __name__  #打印是否为主文件

if __name__ == '__main__':
    print '相等'

print __file__  #打印python文件的目录
print __doc__   #打印最上方用'''注视的内容