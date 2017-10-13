#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#输入数字并逐行打印,打印停止之后访问是否继续,如果继续输入大于之前的数字继续逐行打印,如果输入的数字小于之前的数字打印已经过了,如果不继续就退出.
#【第2课】02 python s8day2 上节作业讲解
import sys

print_num = input('输入的数字:')
count = 0

while count < 1000000:
    if count == print_num:
        print '输入的数字为:',count
        choice = raw_input('是否继续输入,(y/n)')
        if choice == 'n':
            break
        else:
            while print_num <= count:
                print_num = input('输入的数字:')
                if print_num <= count:
                    print '已经过了'
    else:
        print 'loop:',count
        count += 1
else:
    print 'loop:',count