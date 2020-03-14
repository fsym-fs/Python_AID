"""
    建立一个dict数据库,建立一个words数据表
    id word mean
    将单词本的单词插入数据库
"""
import re
import pymysql

f = open("dict.txt", "r")
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='hhh',
    password='223751093',
    database='student', charset='utf8')
cur = db.cursor()
sql = "insert into words(word,mean) values (%s,%s)"
l = []
for line in f:
    t = re.findall(r"(\w+)\s+(.*)", line)[0]
    print(t)
    # l.append(t)

# print(l)
f.close()
cur.close()
db.close()
