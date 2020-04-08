from redis.sentinel import Sentinel

# 生成哨兵连接
sentinel = Sentinel([('localhost', 26379)], socket_timeout=0.1)

# 初始化master连接
master = sentinel.master_for('hhh', socket_timeout=0.1, db=0)
slave = sentinel.slave_for('hhh', socket_timeout=0.1, db=0)

# 使用redis相关命令
master.set('mymaster', 'yes')
print(slave.get('mymaster'))
