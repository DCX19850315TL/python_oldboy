#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2017/11/1 16:26
'''
#需求:
#1.每个客户端需要监控的服务不同
#2.每个服务的监控间隔不同
#3.允许模板的形式批量修改监控指标
#4.不同设备的监控阀值不同
#5.可自定义最近n分钟内hit\max\avg\last\... 指标超过阀值
#6.报警策略，报警等级，报警自动升级
#7.历史数据的存储和优化 时间越久数据越失真
#8.跨机房，跨区域代理服务器
#第三方的socket框架:twisted
