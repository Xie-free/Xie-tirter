# 阻塞式
import os
import random
from multiprocessing import Pool
import time
"""
特点:
    添加一个任务执行一个任务, 如果一个任务不结束另一个任务就进不来
    
    进程池:
    pool = Pool(max)  创建进程池对象
    pool.apply()  阻塞的
    pool.apply_async()  非阻塞的
    
    pool.close()
    pool.join()  让主进程让步
"""



# 非阻塞式进程

def task(task_name):
    print("开始做任务了!", task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random.random() * 2)
    end = time.time()
    print(f"完成任务{task_name}用时:{(end - start)}进程id:{os.getpid()}")
    # return f"完成任务{task_name}用时:{(end - start)}进程id:{os.getpid()}"


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ["听音乐", "吃饭", "洗衣服", "打游戏", "散步", "看孩子", "做饭"]
    for i in tasks:
        pool.apply(task, args=(i,))  # apply_async:非阻塞式
    pool.close()
    pool.join()

    print("over!!!!")