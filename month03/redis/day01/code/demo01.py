import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

# 通用命令

key_list = r.keys('*')
# 返回字节型
for key in key_list:
    print(key)

# 返回值:1 代表存在,0代表不存在
print(r.exists('uname'))

# list #
r.lpush('pyl1', 'a', 'b', 'c', 'd', 'e', 'f')
print(r.lrange('pyl1', 0, -1))

print(r.rpop('pyl1'))

print(r.ltrim('pyl1', 0, 2))

print(r.lrange('pyl1', 0, -1))

# string #

r.set('pyuname', 'Jarry')
print(r.get('pyuname'))

# mset key1 value1 key2 value2
r.mset({'pyun1': 'Tom', 'pyun2': 'Jam'})
print(r.mget('pyun1', 'pyun2'))

r.incr('pyage')
print(r.incrby('pyage', 10))
