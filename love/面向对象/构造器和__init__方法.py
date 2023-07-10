# 函数 和  类里面定义的:

def func(name):
    print("---->", name)


user_name = "xie"
func(user_name)


def func(names):
    for name in names:
        print(name)


name_list = ["aa", "bb", "cc"]
func(name_list)


class Phone:
    # 魔术方法之一: 称作魔术方法__名字__()
    def __init__(self):  # init 初始的, 初始化
        self.brand = "华为"
        self.price = 4999

    def call(self):  # self 是不断 发生改变
        print("----------call")
        print("价格:", self.price)


# p = Phone()
# p.price = 1000
# p.call()  # p.call()   p对象
#
# p1 = Phone()
# p1.call()
p = Phone()