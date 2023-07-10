from threading import Thread


class My_Thread(Thread):
    def run(self):
        print(f"{self.name}正在运行")


t = My_Thread(name="xie")
t.start()