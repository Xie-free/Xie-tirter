import os
from multiprocessing import Process
from time import sleep


def task1(s, name):
    while True:
        sleep(s)
        print("这是任务1.......", os.getpid(), "---------", os.getppid(), name)


def task2(s, name):
    while True:
        sleep(s)
        print("这是任务2.......", os.getpid(), "----------", os.getppid(), name)


if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p = Process(target=task1, name="任务1", args=(1, "aa"))
    p.start()
    print(p.name)
    p1 = Process(target=task2, name="任务2", args=(1, "bb"))
    p1.start()
    print(p1.name)

    print("----------")
    print("***********")
