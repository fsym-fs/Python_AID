"""
    **list案例: 一个进程负责生产任务，一个进程负责消费任务**
"""
import redis
import json

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

json_obj = {'task': 'send_email', 'from': 'ligoucong', 'to': 'licong@qq.com', 'content': 'xxxxx'}

json_str = json.dumps(json_obj)

# 先进先出
r.lpush('pypc', json_str)
