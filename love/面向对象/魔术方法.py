# 魔术方法
# __init__: 初始化魔术方法
# 触发时机: 初始化对象时触发(不是实例化触发, 但是和实例化在一个操作中)

# __new__: 实例化的魔术方法
# 触发时机: 在实例化对时触发

# __call__: 对象调用方法
# 触发时机: 将对象当成函数使用的时候, 会默认调用此函数中内容


class Person:
    def __init__(self, name):
        print("----------->init", self)  # <__main__.Person object at 0x0000024EEE115D10>
        self.name = name

    def __new__(cls, *args, **kwargs):  # __new__ 向内存要空间  ----> 地址
        print("------------>new")
        position = object.__new__(cls)
        print(position)  # <__main__.Person object at 0x0000024EEE115D10>
        return position  # 地址

    def __call__(self, name):
        print("----------->call", self)
        print("执行对象得到参数是:", name)  # 执行对象得到参数是: xie


p = Person("jacker")

print(p)
p("xie")

# def func():
#   pass
#
# func()
