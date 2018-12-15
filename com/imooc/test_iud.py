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

sql_insert = "insert into user(userid,username) values (10,'name10')"
sql_update = "update user set username='name91' where userid=9"
sql_deletd = "delete from user where userid<3"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_deletd)
    print(cursor.rowcount)

    conn.commit()
except Exception as e:
    print(e)
    conn.rollback

cursor.close()
conn.close()
