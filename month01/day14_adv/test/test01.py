"""
使用三种导入方式,导入model01
"""
# import month01.day14_adv.test.module01 as k
# print(k.a)
# f = k.A()
# k.A.show()
# f.show_a()
# from month01.day14_adv.test.module01 import *
# print(a)
# f = A()
# f.show_a()
# A.show()
from month01.day14_adv.test.module01 import A,a
# from month01.day14_adv.test.module01 import a
f = A()
A.show()
f.show_a()
print(a)