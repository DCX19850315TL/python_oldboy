#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: sql_helper.py
@time: 2017/10/23 11:30
'''
import MySQLdb
import conf

class MySqlHelper(object):  #类里面包含增,删,改,查

    def __init__(self):
        self.__conn_dict = conf.conn_dict

    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

        reCount = cur.execute(sql,params)  # 查询表里面总共有多少行数据
        data = cur.fetchall()  # 查询数据内容

        cur.close()
        conn.close()
        return data

    def Get_One(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        reCount = cur.execute(sql, params)  # 查询表里面总共有多少行数据
        data = cur.fetchone()  # 查询数据内容

        cur.close()
        conn.close()
        return data

helper = MySqlHelper()
sql = "select * from admin where id > %s"
params = (1,)

simple_data = helper.Get_One(sql,params)
dict_data = helper.Get_Dict(sql,params)