import jwt
import time

JWT_TOKEN_KEY = '223751093'


def make_token(username, exp=3600 * 24):
    now = time.time()
    payload = {'username': username, 'exp': now + exp}
    return jwt.encode(payload, JWT_TOKEN_KEY, algorithm='HS256')


def de_token(token):
    d_token = jwt.decode(token, JWT_TOKEN_KEY, algorithm='HS256')
    return d_token
