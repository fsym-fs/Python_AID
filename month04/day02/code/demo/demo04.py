import pymysql

db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')

cur = db.cursor()

ins = 'insert into maoyantab values(%s,%s,%s)'
cur.execute(ins,['喜剧之王','周星驰','1993-01-01'])
db.commit()
cur.close()
db.close()