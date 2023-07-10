"""
多进程对于全局变量访问,在每个全局变量里面放一个m变量,
保证每个进程访问变量互不干扰.
m = 1  # 不可变类型
list1 = []  # 可变类型

"""

import os
from multiprocessing import Process
from time import sleep

m = 1  # 不可变类型
list1 = []  # 可变类型


def task1(s, name):
    while True:
        sleep(s)
        global m
        m += 1
        list1.append(str(m) + "task1")
        print("这是任务1.......", m, list1)


def task2(s, name):
    while True:
        sleep(s)
        global m
        m += 1
        list1.append(str(m) + "task2")
        print("这是任务2.......", m, list1)


if __name__ == '__main__':
    # 子进程
    p = Process(target=task1, name="任务1", args=(1, "aa"))
    p.start()

    p1 = Process(target=task2, name="任务2", args=(2, "bb"))
    p1.start()

    while True:
        sleep(1)
        m += 1
        print("----->main", m)
