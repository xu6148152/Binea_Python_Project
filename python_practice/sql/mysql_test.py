# coding=utf-8
__author__ = 'xubinggui'

import mysql.connector
conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

print cursor.rowcount
cursor.execute('select * from user where id=?', '1')
values = cursor.fetchall()
print values

cursor.close()
conn.commit()
conn.close()