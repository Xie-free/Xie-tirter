import threading
from time import sleep

"""
线程是可以共享全局变量的
GIL  全局解释器锁


"""

ticket = 1000


def run1():
    global ticket
    for i in range(100):
        sleep(0.01)
        ticket -= 1


# def run2():
#     global ticket
#     for i in range(100):
#         ticket -= 1


if __name__ == '__main__':
    # 创建线程
    r = threading.Thread(target=run1, name="aa")
    r1 = threading.Thread(target=run1, name="bb")
    r2 = threading.Thread(target=run1, name="cc")
    r3 = threading.Thread(target=run1, name="dd")

    # 启动
    r.start()
    r1.start()
    r2.start()
    r3.start()

    r.join()
    r1.join()
    r2.join()
    r3.join()

    print("money", ticket)
