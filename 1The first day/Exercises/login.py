#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#登陆帐号，看登陆的帐号是否被锁定，如果锁定返回稍后重试，如果没有锁定就到文件存储中匹配用户名和密码，匹配成功打印登陆成功，匹配不成功显示请重新输入并显示可重试次数。
import os
import sys

retry_count = 0
retry_limit = 3
lock_file = 'D:\\2Develop\\python_oldboy\\1The_first_day\\lock_file.txt'
account_file = 'D:\\2Develop\\python_oldboy\\1The_first_day\\account_file.txt'

while retry_count < retry_limit:    #可以重新验证用户名或密码的次数
    username = raw_input('输入用户名:')  #交互式输入用户名

    lock_check = file(lock_file,'r')    #以只读的方式打开lock_file文件

    for line in lock_check.readlines(): #逐行读取lock_file文件的内容
        line = line.split() #将lock_file以空格分割成列表
        if username == line[0]:    #判断如果输入的username在lock_file文件中，就退出并打印你输入的用户名已经被锁定
            sys.exit('你输入的用户名已经被锁定')

    password = raw_input('输入密码:')   #交互式输入密码

    f = file(account_file,'rb')  #以二进制只读模式读取accout_file文件
    match_flag = False  #设置匹配是否成功的标志位，
    for line in f.readlines():  #循环读取account_file文件
        user,passwd = line.strip('\n').split()  #设置变量user和passwd为文件中格式化后的字符串

        if  username == user and password == passwd :  #判断输入的用户名和密码和account_file文件中存储的用户名和密码是否一致，如果匹配上了就进行打印
            print '用户名和密码匹配成功',username
            match_flag = True   #设置匹配标记为True
            break   #跳出这个循环
    f.close()
    if match_flag == False: #如果标记位为False，打印未匹配成功，并进行重试
        print '用户名和密码未匹配成功'
        retry_count += 1    #重试次数加1
    else:
        print '匹配成功，登陆系统'
        sys.exit()
else:
    print '您的用户已经被锁定，请稍后再试' #超过重试次数，打印用户被锁定
    f = file(lock_file,'ab')    #以追加的方式打开lock_file文件
    f.write(username)   #将用户名添加到lock_file文件中
    f.close()