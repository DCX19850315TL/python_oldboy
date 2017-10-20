#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: re_study.py
@time: 2017/10/15 15:24
'''
#正则表达式
import re

#match只能从字符串起始位置开始匹配，search可以在整个内容进行匹配
'''
result1 = re.match('\d+','adfdasf222teeqrq333wer')
if result1:
    print result1.group()
else:
    print 'nothing1'

result2 = re.search('\d+','adfdasfteeqrq222wer')
if result2:
    print result2.group()
else:
    print 'nothing2'
'''

'''
result3 = re.findall('\d+','11adf33da55sfteeqrq222wer')
print result3
'''

'''
com = re.compile('\d+')
print(com.findall('11adf33da55sfteeqrq222wer'))
'''

'''
result4 = re.search('(\d+)adf(\d+)','11adf33da55sfteeqrq222wer')
print result4.group()
print result4.groups()
'''

'''
result5 = re.search('a{3,5}','aaaaa')
print result5.group()
'''

ip = '1.3.4.43242.~dfadfs.192.168.101.100.fdafs.rerqrqrqerqwreqwrwq.fafadsfdafsaf'
print (re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip))

print (re.findall('(?:\d{1,3}\.){3}\d{1,3}',ip))
