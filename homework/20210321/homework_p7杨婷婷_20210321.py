# 1、将python所学内容整理成思维导图
# 2、自己完成以下研究
#     2.1 python连接MySQL数据库进行数据的操作
#     2.2 python实现发送邮件

# !/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.12.195","acg","Euyg#165","ABoutCG")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()