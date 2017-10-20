#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#练习字符串的各种方法

import sys
import os

msg1 = "what's your company's name"
#转换 string 中的小写字母为大写
print(msg1.upper())

msg2 = "what's your company's name"
#把字符串的第一个字符大写
print(msg2.capitalize())

msg3 = "what's your company's name"
#找到your字符串所在的下标位置
print(msg3.find('your'))
print(msg3.index('your'))
#将msg3的字符串按照'符号分割成列表
new_msg = msg3.split('\'')
#将列表以'符号更换为|符号，并变为字符串
print('|'.join(new_msg))