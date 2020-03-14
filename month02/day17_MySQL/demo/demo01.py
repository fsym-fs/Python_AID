"""
    mysql
"""
import pymysql

# 链接数据库
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='hhh',
    password='223751093',
    database='student', charset='utf8')

# 创建游标
cur = db.cursor()

# 执行数据操作


# 关闭游标和数据库
cur.close()
db.close()
