from django.shortcuts import render
import json
from django.http import JsonResponse
import pymysql


# Create your views here.


def indexview(request):
    return render(request, 'forum/topic_index.html')


def topic_publish(request):
    if request.method == 'GET':
        return render(request, 'forum/topic_publish.html')
    elif request.method == 'POST':
        # json_bytes = request.body
        # 将 bytes 类型转为 str
        # json_str = json_bytes.decode()
        # python3.6 及以上版本中, json.loads() 方法可以接收 str 和 bytes 类型
        # 但是 python3.5 以及以下版本中, json.loads() 方法只能接收 str,
        # 3.5 需要有上面的编码步骤.
        req_data = json.loads(request.body)
        title = req_data['title']
        topic = req_data['topic']
        if title and topic:
            # sql = 'insert into forum_topic (title,topic) values (%s,%s)'
            # db = pymysql.connect(
            #     host='127.0.0.1',
            #     user='root',
            #     password='123456',
            #     database='kjlt',
            #     charset='utf8',
            # )
            # cur = db.cursor()
            # cur.execute(sql, [title, topic])
            # db.commit()
            # cur.close()
            # db.close()
            return JsonResponse({'code': 200})
