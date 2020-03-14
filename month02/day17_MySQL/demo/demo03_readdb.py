"""
    read_db
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

name = input("Name:")

# 执行数据操作

# 查询数据库
sql = "select name,age,score from cls;"
sql1 = "select name,age,score from cls where name = '%s';" % name
sql2 = "select * from cls where name = %s or score > %s;"
# 只可传递数据参量
cur.execute(sql2, [name, 90])

print(cur.fetchall())

# 关闭游标和数据库
cur.close()
db.close()
