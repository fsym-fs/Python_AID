import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

r.hset('pyh1', 'name', 'Lily')
print(r.hget('pyh1', 'name'))

r.hmset('pyh1', {'age': 15, 'desc': 'haha'})
print(r.hgetall('pyh1'))

# set

r.sadd('pys1', 'a', 'b', 'c', 'd', 'e', 'f')
print(r.smembers('pys1'))
m1 = r.spop('pys1')
print(m1)
r.sadd('pys2', 'a', 'b', 'c')
print(r.sinter('pys1', 'pys2'))

# sorted_set
r.zadd('pyz1', {'tom': 8000, 'lily': 12000})
# [(b'tom', 8000.0), (b'lily', 12000.0)]
print(r.zrange('pyz1', 0, -1, withscores=True))
r.zadd('pyz2', {'tom': 5000})
r.zinterstore('pyz3', ('pyz1', 'pyz2'), aggregate='max')
print(r.zrange('pyz3', 0, -1, withscores=True))
