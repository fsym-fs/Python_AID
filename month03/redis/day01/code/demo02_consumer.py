"""
    **list案例: 一个进程负责生产任务，一个进程负责消费任务**
"""
import redis
import json

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

while True:
    task = r.brpop('pypc', 5)
    print('task:',task)
    if task:
        json_obj = json.loads(task[1])
        print(json_obj)
