#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#列表是有序的,可以进行增删该查.
#找出列表中2的下标位有几个,并显示下标位置.
import sys

name = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,]

first_pos = 0

for i in range(name.count(2)):
    new_list = name[first_pos:]
    print '2 is index :',first_pos + new_list.index(2)
    next_pos = new_list.index(2) + 1
    first_pos += next_pos


