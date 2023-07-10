from multiprocessing import Process
from threading import Thread

# def func():
#     for i in range(1000):
#         print("子进程:", i)
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#
#     for i in range(1000):
#         print("主进程:", i)


def func(name):  # 传参
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    t = Thread(target=func, args=("周杰伦",))  # 传参必须是元组
    t.start()

    t1 = Thread(target=func, args=("张震岳",))
    t1.start()