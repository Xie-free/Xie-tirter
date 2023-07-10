import threading

n = 0


def task1():
    global n
    for i in range(100000000):
        n += 1
    print("-------task1中的n值是", n)


def task2():
    global n
    for i in range(100000000):
        n += 1
    print("-------task2中的n值是", n)


if __name__ == '__main__':
    th = threading.Thread(target=task1, name="aa")
    th1 = threading.Thread(target=task2, name="bb")

    th.start()
    th1.start()

    th.join()
    th1.join()

    print("最后打印n:", n)
