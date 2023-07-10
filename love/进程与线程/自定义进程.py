# 进程:  自定义
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    # 重写run方法
    def run(self):
        n = 1
        while True:
            # print("进程名:"+self.name)
            print(f"{n, self.name}-----------自定义进程")
            n += 1


if __name__ == '__main__':
    p = MyProcess("小谢")
    p.start()

    p1 = MyProcess("小灯")
    p1.start()
