# 递归函数:
"""
普通: def func() : pass
匿名函数: lambda 参数: 返回结果
递归函数: 普通函数的一种表现方式

特点:
1. 递归函数必须设定终点
2. 通常都会有一个入口
"""


def sum_num(n):  # 1~n
    if n == 0:
        return n
    else:
        return n + sum_num(n - 1)


def sum1(n):
    if n == 100:
        return n
    else:
        return n + sum1(n + 1)


result = sum_num(10)

print(result)

result = sum1(0)

print(result)