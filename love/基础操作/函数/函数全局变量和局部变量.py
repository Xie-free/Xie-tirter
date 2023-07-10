"""
全局和局部变量:
声明函数外面的称作全局变量
声明在函数内部的变量,称作局部变量

函数内部可以直接使用全局变量, 但是不能直接修改全局变量
如果想修改全局变量, 则必须使用关键字: global 全局变量声明

****全局变量和局部变量:
global关键字的添加:
只有不可变的类型才需要添加global
可变类型不需要添加global
"""
a = 100


def test():
    a = 0
    b = 8
    print("a = ", a)
    print("b = ", b)


def test1():
    # 局部变量的作用范围仅限宇函数内部
    b = 9
    print("a = ", a)
    print("b = ", b)


def test2():
    # 改变全局a的值
    # a = 10  # 声明一个局部变量a
    global a
    a -= 10
    print("a = ", a)


test1()
test()
test2()
