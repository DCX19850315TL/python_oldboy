#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2017/11/2 11:04
'''
import redis
'''
conn = redis.Redis(host='192.168.137.2',port=6379,db=0)
conn.set('test', 'redis test')
print conn.get('test')
'''
class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='192.168.137.2')
        self.chan_sub = 'fm87.7'
        self.chan_pub = 'fm87.7'

    def __get__(self,key):
        return self.__conn.get(key)

    def __set__(self,key,value):
        self.__conn.set(key,value)

    def public(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

if __name__ == '__main__':
    t = RedisHelper()
    t.public('test')