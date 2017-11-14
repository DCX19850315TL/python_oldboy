#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: server1.py
@time: 2017/11/2 15:21
'''
import index

r = index.RedisHelper()
recv = r.subscribe()
recv.parse_response()