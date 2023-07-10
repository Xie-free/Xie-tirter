"""
闭包:
1. 嵌套函数
2. 内部函数引用外部函数的变量
3. 返回值是内部函数

"""


def outer(n):
    a = 10

    def inner():
        b = a + n
        print("内", b)

    return inner


result = outer(5)  # result 获取了inner的地址
print(result)

result()

# 查看全局变量
print(globals())

# 查看局部变量
print(locals())