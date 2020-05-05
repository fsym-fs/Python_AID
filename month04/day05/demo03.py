"""
    json.dump()
    将数据设置为json格式并存入到本地json文件中
"""
import json

all_file_list = [
    {'rank': '1', 'name': '霸王别姬', 'start': '张国荣'},
    {'rank': '2', 'name': '大话西游', 'start': '周星驰'},
]
with open('file.json', 'w',encoding='utf8') as f:
    json.dump(all_file_list, f, ensure_ascii=False)
