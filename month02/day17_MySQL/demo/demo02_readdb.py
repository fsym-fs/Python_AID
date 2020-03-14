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

# 执行数据操作

# 查询数据库
sql = "select name,age,score from cls;"
cur.execute(sql)

# 获取结果法一,获取一个少一个
for i in cur:
    print(i)

# 获取结果法二
i = cur.fetchone()
print(i)

# 获取结果法三
print(cur.fetchall())

# 获取结果法四
print(cur.fetchmany(2))

# 关闭游标和数据库
cur.close()
db.close()
