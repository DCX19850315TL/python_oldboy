#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#登陆帐号，看登陆的帐号是否被锁定，如果锁定返回稍后重试，如果没有锁定就到文件存储中匹配用户名和
#密码，匹配成功打印登陆成功，匹配不成功显示请重新输入并显示可重试次数。
import os
import sys

retry_count = 0
retry_limit = 3
lock_file = 'D:\\2Develop\\python_oldboy\\lock_file.txt'
accout_file = 'D:\\2Develop\\python_oldboy\\accout_file.txt'

while retry_count < retry_limit:
    username = raw_input('输入用户名:')

    lock_check = file(lock_file,'r')

    for line in lock_check.readlines():
        if username in line:
            sys.exit('你输入的用户名')