# 线程
"""
    考虑?  创建线程?  如何使用线程?
    t = threading.Thread(target=down_load, name="aa", args=(1,))
    t.start()

    线程:
    新建  就绪  运行  阻塞  结束


"""

import threading

# 进程:  Process
# 线程:  Thread
from time import sleep


def down_load(n):
    images = ["girl.jpg", "boy.jpg", "man.jpg"]
    for image in images:
        print("正在下载", image)
        sleep(n)
        print(f"下载{image}成功")


def listen_Music():
    musics = ["晴天", "稻香", "夜曲", "七里香"]
    for music in musics:
        sleep(0.5)
        print(f"正在听{music}")


if __name__ == '__main__':
    # 线程对象
    t = threading.Thread(target=down_load, name="aa", args=(1,))
    t.start()

    t1 = threading.Thread(target=listen_Music, name="bb")
    t1.start()

    # a = 1
    # while True:
    #     sleep(1.5)
    #     print(a)
    #     a += 1
