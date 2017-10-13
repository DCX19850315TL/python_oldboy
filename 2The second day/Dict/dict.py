#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#基本字典的形式,字典里面的key是唯一的。

import sys
import os
import copy

name_info = {
    'name' : 'tanglei',
    'age' : 30,
    'job' : 'IT'
}
print(name_info['name'])

#字典的方法演示
# name_info['aaa'] = 123  #插入新的key value值到字典中
# name_info['job'] = 'bbb'    #更改job这个key的值为bbb
# name_info.pop('job')    #删除job这个key和对应的value
# name_info.popitem() #随即删除一个key:value
name_info['GF'] = ['wutenglan','hehe']  #以列表的形式增加一个key:value
info2 = name_info.copy()    #浅复制name_info的内容到info2中,如果name_info列表中的内容有变，info2列表中的内容不变
print name_info,info2

info3 = copy.deepcopy(name_info)    #深复制name_info的内容到info2中,如果name_info列表中的内容有变，info2列表中的内容也变
# for i in name_info:     #循环打印name_info的key:value，效率高
#     print i,name_info[i]

# for k,v in name_info.items():   #循环打印name_info的key:value，效率低，因为需要先转成列表
#     print k,v