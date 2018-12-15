# -*- coding:UTF-8 -*-
'''
Created on 2018��11��28��

@author: samsung
'''
import pymysql
from _sqlite3 import Cursor

conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123456aaa',
    db = 'imooc',
    charset = 'utf8'
    )

cursor =conn.cursor()

#创建一个sql语句
sql = "select * from user"
#调用cursor。execute方法，执行sql语句，并将结果保存在本地缓冲区
cursor.execute(sql)
#打印所有结果
print(cursor.rowcount)
#将第一条数据放入rs这条变量
rs = cursor.fetchone()
print(rs)
rs = cursor.fetchmany(3)
print(rs)
rs = cursor.fetchall()
print(rs)


print(conn)
print(cursor)

cursor.close()
conn.close()
