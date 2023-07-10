"""
实现多任务的方式:
---- 多进程模式
---- 多线程模式
---- 协程
    进程  >  线程  > 协程

    from multiprocessing import Proces

    process = Process(target= 函数, name=进程名, args=(给函数传递的参数))
    process 对象

    对象调用方法:
    process.start()  启动进程并执行任务
    process.run()  只是执行了任务但是没有启动进程
    terminate()  终止
"""

# 进程创建
import os
from multiprocessing import Process
from time import sleep


def task1():
    while True:
        sleep(1)
        print("这是任务1.......", os.getpid(), "---------", os.getppid())


def task2():
    while True:
        sleep(2)
        print("这是任务2.......", os.getpid(), "----------", os.getppid())


number = 1
if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p = Process(target=task1, name="任务1")
    p.start()
    print(p.name)
    p1 = Process(target=task2, name="任务2")
    p1.start()
    print(p1.name)

    while True:
        number += 1
        sleep(0.1)
        if number == 100:
            p.terminate()
            p1.terminate()
            break
        else:
            print("--------------->number", number)

    print("----------")
    print("***********")
