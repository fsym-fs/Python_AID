import hashlib
import base64

# s1 = b'hxy'
#
# m = hashlib.sha256()
#
# m.update(s1)
# ms = m.hexdigest()
# print(ms)
# print(len(ms))
s = b'lg'
m = base64.urlsafe_b64encode(s)
m = m.replace(b'=',b'')
print(m)
l = len(m)
l1 = 4-len(m)
m = m+b'='*l1
print(m)
s1 = base64.b64decode(m)
print(s1)

# a = '123.4569.789'
# b,c,d = a.split('.')
# print(b)