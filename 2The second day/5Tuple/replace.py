#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import sys
import os

if len(sys.argv) != 3:
    parameter = "usage:./replace.py old_text new_text file_name"
    a = list(parameter)
    print(parameter.split())

old_text = a.argv[1]
# new_text = sys.argv[2]
# file_name = sys.argv[3]
#
# f = file('D:\\2Develop\\python_oldboy\\2The_second_day','rb')
# for line in f.xreadlines():
#     print line.replace(old_test,new_text)
