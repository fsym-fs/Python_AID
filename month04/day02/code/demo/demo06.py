import pymongo

# 1.连接对象
conn = pymongo.MongoClient(host='localhost', port=27017)
# 2.库对象
db = conn['maoyandb']
# 3.集合对象
myset = db['maoyanset']
# 4.插入数据库
myset.insert_one({'name': '那些年','start':'ABC','time':'2009-02-02'})
# myset.insert_many([{'name': '小昭'}, {'age': '30'}])
