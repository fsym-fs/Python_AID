"""
    time
"""
import time

a = time.localtime()
b = time.time()
print(b)
print(a)
# c = time.localtime(b)
# print(c)
# d = time.mktime(a)
# print(d)
# #时间元组--->自定义字符串格式时间
# s = time.strftime()
# #时间元组<---自定义字符串格式时间
# time.strptime()