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

sql = "select * from user"
cursor.execute(sql)

rs = cursor.fetchall()
for row in rs:
    print("userid=%s,username=%s" % row)
    

cursor.close()
conn.close()
