#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#将test1.txt文件中的内容去掉回车符，并以:符号做成列表的形式。
import sys
import os

f = file('D:\\2Develop\\python_oldboy\\test1.txt','r')
for line in f.readlines():
    line = line.strip('\n').split(':')
    print line

#练习文件的各种方法
#test2.txt以写入的模式打开，并往文件中写入aaa字符串
g = file('D:\\2Develop\\python_oldboy\\test2.txt','w')
g.write('aaa')
#test2.txt以追加的模式打开，并往文件中追加bbb字符串
h = file('D:\\2Develop\\python_oldboy\\test2.txt','a')
h.write('\nbbb')
