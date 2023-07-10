__all__ = ["add", "number", "Calculate"]

# 变量
number = 100
name = "calculation"


# 函数
def add(*args):
    if len(args) > 1:
        num = 0
        for i in args:
            num += i
        return num
    else:
        print("至少传两个参数.....")
        return args


def minus(*args):
    if len(*args) > 1:
        m = 0
        for i in args:
            m -= i
    else:
        print("至少传入两个参数")


def multiply(*args):
    pass


def divide(*args):
    pass


# 类
class Calculate:
    def __init__(self, num):
        self.n = num

    def test(self):
        print("正在使用Calculate运算......")

    @classmethod
    def test1(cls):
        print("---------> Calculate中类方法")


def test():
    print("我是测试----------------")


print("__name__:", __name__)
if __name__ == '__main__':
    print(__name__)  # __name -----> __main__
    test()
