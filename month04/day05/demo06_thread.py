"""
    多线程
"""

from threading import Thread


def spider():
    print('I am spider')


t_list = []

for i in range(5):
    t = Thread(target=spider)
    t_list.append(t)
    t.start()
    # j.json()
for i in t_list:
    i.join()
