import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, password='123456')

r = redis.Redis(connection_pool=pool)


def double_account(user_id):
    key = 'account_%s' % (user_id)
    with r.pipeline() as pipe:
        while True:
            try:
                # watch key
                pipe.watch(key)
                value = int(r.get(key))
                value *= 2
                print('value is %s ' % (value))
                pipe.multi()
                pipe.set(key, value)
                pipe.execute()
                break
            except:
                pass
