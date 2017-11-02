#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: multiprocess_study1.py
@time: 2017/10/20 16:10
'''
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='08day5')
cur = conn.cursor()

reCount = cur.execute('select * from admin')    #查询表里面总共有多少行数据
data = cur.fetchall()   #查询数据内容

cur.close()
conn.close()

print reCount
print data
'''
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='08day5')
cur = conn.cursor()

sql = 'insert into admin (name,address) values(%s,%s)'
params = ('alex_1','usa')
reCount = cur.execute(sql,params)
conn.commit()

cur.close()
conn.close()
'''
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='08day5')
cur = conn.cursor()

sql = 'delete from admin where id = %s'
params = (1,)
reCount = cur.execute(sql,params)
conn.commit()

cur.close()
conn.close()
'''
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='08day5')
cur = conn.cursor()

sql = 'update admin set name = %s where id = 2'
params = ('aa',)
reCount = cur.execute(sql,params)
conn.commit()

cur.close()
conn.close()
'''
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='08day5')
cur = conn.cursor()

li = [
    ('alex','usa'),
    ('bb','usa'),
]
reCount = cur.executemany('insert into admin(name,address) values(%s,%s)',li)
conn.commit()

cur.close()
conn.close()

print reCount
'''
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='08day5')
#cur = conn.cursor()
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

reCount = cur.execute('select * from admin')    #查询表里面总共有多少行数据
data = cur.fetchall()   #查询数据内容

cur.close()
conn.close()

print reCount
print data
'''
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='08day5')
#cur = conn.cursor()
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

reCount = cur.execute('select * from admin')    #查询表里面总共有多少行数据
#data = cur.fetchall()   #查询数据内容
data = cur.fetchone()
print data

data = cur.fetchone()
print data

#cur.scroll(-1,mode='relative')     #相对定位
#cur.scroll(0,mode='absolute')   #绝对定位


cur.close()
conn.close()
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='08day5')
cur = conn.cursor()

sql = 'insert into media (media) values(%s)'
params = ('/usr/bin/aa',)
reCount = cur.execute(sql,params)
conn.commit()
new_id = cur.lastrowid
sql = 'insert into content (title,content,media_id) values(%s,%s,%s)'
params = ('test','content',new_id)
reCount = cur.execute(sql,params)
conn.commit()

cur.close()
conn.close()