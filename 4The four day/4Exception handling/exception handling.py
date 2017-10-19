#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: setter.py
@time: 2017/10/18 15:59
'''
from web import account

'''
login = raw_input('输入:')
array = login.split('/')
try:
    model = __import__('web.'+array[0])
    aa = getattr(model,array[0])
    func = getattr(aa,array[1])
    func()
#except (ImportError,AttributeError),e:  #捕捉两个错误
    #print e
    #print '跳转到自定义的404'

except ImportError,e:   #将捕捉的的错误分开显示
    print 1,e
    print '跳转到自定义的404'
except AttributeError,e:
    print 2,e
    print '跳转到自定义的404'
except Exception,e: #全部错误都进行捕捉
    print 3,e
    print '跳转到自定义的404'

else:
    print '没有出错'    #没有捕捉到错误执行

finally:
    print '有没有捕捉到错误都执行'
'''

#自定义异常，继承Exception类就可以自定义异常
'''
class MyException(Exception):

    def __init__(self,msg):
        self.error = msg

    def __str__(self,*args,**kwargs):
        return '该对象是MyException类实例化的一个对象'

obj = MyException('错误')
print obj
'''

class MyException(Exception):

    def __init__(self,msg):
        self.error = msg

    def __str__(self,*args,**kwargs):
        return self.error

#obj = MyException('自定义错误')
#print obj

#手动触发异常
'''
raise MyException('自定义错误')
'''

def Validate(name,pwd):

    if name == 'alex' and pwd == '123'
        return True
    else:
        return False
try:
    res = Validate('alex','456')
    if res:
        print '登陆成功'
    else:
        #print '记录日志到数据库'
        #print '登陆失败'
        raise Exception('登陆失败')
except Exception,e:
    print '记录日志到数据库'
    print e

