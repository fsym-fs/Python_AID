from multiprocessing import Process
from time import sleep


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I am %s" % name)


p = Process(target=worker, args=(2, 'Lucy'))
p = Process(target=worker,kwargs={"sec":2,"name":"Tome"})
p.start()
p.join()
