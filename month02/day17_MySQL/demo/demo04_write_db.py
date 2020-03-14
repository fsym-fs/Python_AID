"""
    write_db
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

# 执行数据操作(增删改)
try:
    sql1 = "insert into cls values(15,'Joy',13,'m',84);"
    sql2 = "update cls set score = %s where id = %s;"
    cur.execute(sql1)
    cur.execute(sql2, [100, 2])
    db.commit()
except:
    db.rollback()
sql2 = "select * from cls;"
cur.execute(sql2)
print(cur.fetchall())
# 关闭游标和数据库
cur.close()
db.close()
