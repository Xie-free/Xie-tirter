"""
生产者与消费者:两个线程之间的通信
Python的queue模块中提供J同步的、线程安全的队列类，包括FIF0 (先入先出)队列Queue,
LIFO (后入先出)队列LifoQueue, 和优先级队列PriorityQueue。 这些队列都实现]锁原语
(可以理解为原子操作，即要么不做，要么就做完)，能够在多线程中直接使用。

"""
import threading
import queue
import random
import time


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put(f"生产者产生的数据:{num}")
        print(f"生产者产生的数据:{num}")
        time.sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"消费者获取到{item}")
        time.sleep(4)
    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)  # 先进先出
    arr = []

    # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    th.join()
    tc.join()
    print("End")

"""
线程: Thread

1. 创建线程
    A. t = Thread(target=fnc, name="", args=(), kwargs={})  新建状态
        t.start()   -----> 就绪状态
        
        run()
        join()  主进程让步
    B. 自定义线程
    class My_Thread(Thread):
        def run(self):
            任务
        
    t = My_Thread(name="")
    t.start
    
2. 数据共享
    进程共享数据与线程共享数据区别:
        进程是每个进程中都有一份
        线程是共同一个数据  ----->  数据安全性问题
        
    GIL  ----->  伪线程
    
    lock = Lock()  添加锁
    lock.acquire()
    ......
    lock.release()  释放锁
    
    ----->  只要用锁: 死锁
    避免死锁
3. 线程间通信:  生产者与消费者
    生产者: 线程
    消费者: 线程
    import queue
    
    q = queue.Queue()
    # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()
    
    q.put()
    q.get()
    
扩张: GIL
"""