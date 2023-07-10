# 进程间通信
from multiprocessing import Process, Queue
from time import sleep


def down_load(q):
    images = ["girl.jpg", "boy.jpg", "man.jpg"]
    for image in images:
        print("正在下载", image)
        sleep(0.5)
        q.put(image)


def get_file(q):
    while True:
        try:
            file = q.get(timeout=5)
            print(f"{file}保存成功!")
        except:
            print("全部保存完毕")
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=down_load, args=(q,))

    p2 = Process(target=get_file, args=(q,))

    p1.start()
    p2.start()

    print("00000000")
