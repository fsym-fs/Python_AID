# -*- coding:utf-8 -*-
import requests
import json
# def send_template_sms(phone, code):
#     req_url = "http://api.feige.ee/SmsService/Template"
#
#     data = {"Account": "账号", "Pwd": "接口密钥", "Content": code,
#             "Mobile": phone, "TemplateId": 模板id, "SignId": 签名id}
#
#     response = requests.post(req_url, data=data)
#
#     print(response.content)

import random

result = ''
code_str = ''


def send_common_sms(phone, code):
    req_url = "http://api.feige.ee/SmsService/Send"
    data = {"Account": "15851702713", "Pwd": "acca484b9b0f27c010949079f", "Content": "验证码:" + code,
            "Mobile": phone, "SignId": "260952"}

    response = requests.post(req_url, data=data)

    return json.loads(response.content)
    # return response.content

# if __name__ == "__main__":
#     # send_template_sms("13012345678", "1234")
#     for i in range(4):
#         code_str += str(random.randint(0,9))
#     print(code_str)
#     send_common_sms("15851702713", code_str)
