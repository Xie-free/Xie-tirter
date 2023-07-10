# 死锁
"""
开发过程中使用线程, 在线程间共享多个资源的时候
如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不做任何事情

避免死锁:
解决:
1. 重构代码
2. 使用timeout参数
"""
from threading import Thread, Lock
import time

lockA = Lock()
lockB = Lock()


class My_Thread(Thread):
    def run(self):  # start()
        if lockA.acquire():  # 如果可以获取锁则返回True
            print(f"{self.name}获取了A锁")  # 默认取名Thread-1， 依次类推
            time.sleep(0.5)
            if lockB.acquire(timeout=5):  # 阻塞
                print(f"{self.name}获取了B锁, 原来还有A锁")
                lockB.release()
            lockA.release()


class My_Thread1(Thread):
    def run(self):  # start()
        if lockB.acquire():  # 如果可以获取锁则返回True
            print(f"{self.name}获取了B锁")
            time.sleep(0.5)
            if lockA.acquire(timeout=5):
                print(f"{self.name}获取了A锁, 原来还有B锁")
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = My_Thread()
    t2 = My_Thread1()

    t1.start()
    t2.start()
