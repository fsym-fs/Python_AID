"""
3.
    一个目录，在目录下有若干个文件（有子目录和普通文件）。编程将该目录下的普通文件复制到
   家目录下的'备份'这个文件夹中。

    * 提前建立好这个备份文件夹
    * os.path.isfile()
"""
"""
作业：  使用多线程拷贝一个目录，要求同时拷贝该目录下的这些文件

     比如 原目录 --》 os.listdir()（10个文件）
         os.mkdir()  --》 新目录
         创建10个线程，同时拷贝这些文件，将这些文件拷贝到新目录
"""
import os
import time


def cp_dir_file(dir_path, target_path):
    s_time = time.time()
    if os.path.isdir(target_path):
        pass
    else:
        os.mkdir(target_path)
    for i in os.listdir(dir_path):
        if os.path.isfile(dir_path + "/" + i):
            with open(dir_path + "/" + i, "r") as f:
                with open(target_path + "/" + i, "w") as f1:
                    for line in f:
                        f1.write(line)
    print("复制完成!")
    print(time.time() - s_time)


cp_dir_file("../demo", "../chat")

