#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: multiprocess_study1.py
@time: 2017/10/23 11:25
'''
#三层结构如下：
#数据访问层
#业务处理层
#表示层，UI层
#执行顺序：index——model(Admin.py)——utility(sql_helper.py)——数据库(mysql)
#index.py：主程序
#conf.py：配置文件
#model模块：数据库中有几张表，这里就要有几个文件
#utility模块：公共的功能，比如对数据库的操作
from model.admin import Admin

def main():

    user = raw_input('username:')
    pwd = raw_input('password:')
    admin = Admin()
    result = admin.CheckValidate(user,pwd)
    if not result:
        print '用户名或者密码错误'
    else:
        print '登陆后台管理界面'

if __name__ == '__main__':
    main()