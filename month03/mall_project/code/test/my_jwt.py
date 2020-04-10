import json
import time
import base64
import hmac
import copy


class Jwt:
    def __init__(self):
        pass

    @staticmethod
    def encode(my_payload, key, exp=300):
        header = {
            'alg': 'HS256',
            'typ': 'JWT'
        }
        payload = copy.deepcopy(my_payload)
        payload['exp'] = time.time() + exp
        header = base64.urlsafe_b64encode(json.dumps(header, separators=(',', ':'), sort_keys=True).encode())
        payload = base64.urlsafe_b64encode(json.dumps(payload, separators=(',', ':'), sort_keys=True).encode())
        str = header + b'.' + payload
        h = hmac.new(key.encode(), str, digestmod='SHA256')
        sign = h.digest()  # 获取最终结果
        jwt = header + b'.' + payload + b'.' + base64.urlsafe_b64encode(sign)
        return jwt


# https://jwt.io/
a = Jwt()
print(a.encode({'username': 'ligoucong'}, '123456'))
