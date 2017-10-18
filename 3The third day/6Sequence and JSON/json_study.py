#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: json_study.py
@time: 2017/10/15 15:02
'''
#JSON标准化的数据格式。
#区别一:pickle只能在python语言中用，JSON是所有语言都支持。
#区别二:pickle不单可以序列化常规的数据类型，还可以序列化类和对象，JSON只能序列化常规的数据类型（列表，字典，集合，元组）。
#区别三:pickle序列化后人无法读取，JSON序列化后人是可以直接读取的。
#xml存储空间比JSON的存储空间占用量大很多。
import json
import pickle

name_dic = {'name':'tanglei'}
print(json.dumps(name_dic))
print(pickle.dumps(name_dic))

serialized_obj = json.dumps(name_dic)
print(json.loads(serialized_obj))