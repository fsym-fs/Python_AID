# import base64
#
# s = '李聪'
#
# h = base64.b64encode(s.encode())
#
# d = base64.b64decode(h)
#
# print(d.decode())
#
# ma = max(100,500)
# print(ma)
#
import jwt
import time

JWT_TOKEN_KEY = '341107'


def make_token(username, exp=3600 * 24*10000*366):
    now = time.time()
    payload = {'username': username, 'exp': now + exp}
    return jwt.encode(payload, JWT_TOKEN_KEY, algorithm='HS256')


def de_token(token):
    d_token = jwt.decode(token, JWT_TOKEN_KEY, algorithm='HS256')
    return d_token

# a = make_token('韩孝瑶爱李岚婷')
# print(a)
# print(de_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ilx1OTdlOVx1NWI1ZFx1NzQ3Nlx1NzIzMVx1Njc0ZVx1NWM5YVx1NWE3NyIsImV4cCI6MzE3ODE0MDYzNTgzLjEzNjM1fQ.3md-oL-UioPrnzQElD_ipHL1edHYrFb-2hZpAElsT38'))

# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ilx1OTdlOVx1NWI1ZFx1NzQ3Nlx1NzIzMVx1Njc0ZVx1NWM5YVx1NWE3NyIsImV4cCI6MzE3ODE0MDYzNTgzLjEzNjM1fQ.3md-oL-UioPrnzQElD_ipHL1edHYrFb-2hZpAElsT38