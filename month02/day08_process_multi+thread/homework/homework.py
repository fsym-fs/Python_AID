"""
作业：  使用多线程拷贝一个目录，要求同时拷贝该目录下的这些文件

     比如 原目录 --》 os.listdir()（10个文件）
         os.mkdir()  --》 新目录
         创建10个线程，同时拷贝这些文件，将这些文件拷贝到新目录
"""
import os
import time
from threading import Thread


def cp_one(dir_path, target_path):
    s_time = time.time()
    if os.path.isdir(target_path):
        pass
    else:
        os.mkdir(target_path)
    for i in os.listdir(dir_path):
        if os.path.isfile(dir_path + "/" + i):
            os.system("cp " + dir_path + "/" + i + " " + target_path + "/" + i)
        time.sleep(2)
    print("复制完成!")
    print(time.time() - s_time)


def cp_dir_file(dir_path, target_path):
    s_time = time.time()
    if os.path.isdir(target_path):
        pass
    else:
        os.mkdir(target_path)
    for i in os.listdir(dir_path):
        copy_file(dir_path + "/" + i, target_path + "/" + i, "r", "w")
    print(time.time() - s_time)


def copy_file(dir_path, target_path, r_way, w_way):
    if os.path.isfile(dir_path):
        with open(dir_path, r_way) as f:
            with open(target_path, w_way) as f1:
                for line in f:
                    f1.write(line)
    print("复制完成")
    time.sleep(2)


def cp_one_file(dir_path, target_path):
    s_time = time.time()
    if os.path.isdir(target_path):
        pass
    else:
        os.mkdir(target_path)
    file_list = os.listdir(dir_path)
    thread_list = []
    for i in range(len(file_list)):
        t = Thread(target=copy_file, args=(dir_path + "/" + file_list[i], target_path + "/" + file_list[i], "r", "w"))
        t.start()
        thread_list.append(t)
    for i in thread_list:
        i.join()
    print(time.time() - s_time)


"""
    0.003740549087524414
    0.01598834991455078
    
    20.120216846466064
    20.037971258163452
    2.0251917839050293
"""
# cp_one("../demo.sql/", "cp_1")
# cp_dir_file("../demo.sql", "cp_one")
# cp_one_file("../demo.sql", "cp_two")
