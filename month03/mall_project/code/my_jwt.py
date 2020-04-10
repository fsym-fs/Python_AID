import json
import time
import base64
import hmac
import copy


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(my_payload, key, exp=300):
        # 初始化header
        header = {'typ': 'JWT', 'alg': 'HS256'}
        # separators:第一个参数为每个键用什么分割,第二个参数为每个键与值用什么分割
        # sort_keys: 设置排序
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        header_bs = Jwt.b64encode(header_json.encode())
        # init payload
        payload = copy.deepcopy(my_payload)
        payload['exp'] = exp + time.time()
        payload_json = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_json.encode())
        # init sign
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        hm_bs = Jwt.b64encode(hm.digest())
        return header_bs + b'.' + payload_bs + b'.' + hm_bs

    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')

    @staticmethod
    def b64decode(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'=' * (4 - rem)
        return base64.urlsafe_b64decode(b_s)

    @staticmethod
    def decode(token, key):
        header_bs, payload_bs, sign_bs = token.split(b'.')
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        if Jwt.b64encode(hm.digest()) != sign_bs:
            raise
        # 校验时间
        payload_j = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_j)
        exp = payload['exp']
        now = time.time()
        if now > exp:
            raise
        return payload


if __name__ == '__main__':
    # https://jwt.io/
    '''
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODY1MDkxNTUuNjU4MzI1LCJ1c2VybmFtZSI6IlRvbSJ9.EkA7uvt4l2LeO592LmTW_S9JV1HrWmfg6tY--SWIlIk
    '''
    s = Jwt.encode({'username': 'Tom'}, '123456')
    print(s)

    res = Jwt.decode(s, '123456')
    print(res)
