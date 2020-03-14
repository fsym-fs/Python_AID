# """
# 扩展练习：
# * 扩展点
#   1. 百度AI接口使用
#
# * 题目要求
#   1. 编写一组程序，分为客户端和服务端
#   2. 从客户端发送一个图片及图片的类别信息给服务端
#   3. 服务端返回给客户端该图片的识别结果，在客户端打印出来
#
# * 注意点
#   * 粘包的处理
import requests
import base64
import json

ai_list = {'植物': '/v1/plant', '动物': '/v1/animal', '其他': '/v2/advanced_general'}


def baidu(type, path):
    if type in ai_list:
        url = "https://aip.baidubce.com/rest/2.0/image-classify%s?access_token=24.1539b3eb39770cd65a9e46c5d55ad630.2592000.1584179062.282335-18463001" % (
            ai_list[type])
    else:
        return None

    header = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {}
    with open(path, 'rb') as f:
        image = base64.b64encode(f.read())
        data['image'] = str(image, 'utf-8')
        res = requests.post(url=url, data=data, headers=header).text
        return json.loads(res).get('result', 'Error')


# if __name__ == '__main__':
#     print(baidu('植物', 'sc.jpeg'))
