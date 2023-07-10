"""
嵌套:


闭包:


"""


def outer():
    a = 100

    def inter():
        b = 200
        # b += a  # 内部函数可以使用外部函数的变量
        nonlocal a  # 如果想修改外部函数的变量, 需要在内部函数中添加:nonlocal
        a += b  # 内部函数不能修改外部函数的变量
        print("内", b)

    # result = locals()  # locals()  表示查看函数中的局部变量, 以字典的形式返回
    # print(result)
    print(a)
    # 调用inter
    inter()


outer()


# 内层函数 ---->  外层函数  ------> 全局 ------> 系统 builtins