#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2017/10/29 11:56
'''
import paramiko

ssh = paramiko.SSHClient
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #自动增加签名到ssh/known_hosts
ssh.connect('192.168.12.91',22,'root','123456')
stdin,stdout,stderr =  ssh.exec_command('df')
print stdout.read()
ssh.close()