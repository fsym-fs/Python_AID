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
# 插入数据
l = [
    ('Dave', 15, 'm', 81),
    ('Ala', 13, 'w', 79),
    ('Eva', 14, 'w', 91),
    ('Baron', 13, 'm', 61)
]

# 执行数据操作(增删改)
sql1 = "insert into cls (name,age,sex,score) values(%s,%s,%s,%s);"
try:
    # for i in l:
    #     cur.execute(sql1, i)
    cur.executemany(sql1, l)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
sql2 = "select * from cls;"
cur.execute(sql2)
print(cur.fetchall())
# 关闭游标和数据库
cur.close()
db.close()
