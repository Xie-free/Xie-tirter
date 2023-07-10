generator = (i * 3 for i in range(10))

while True:
    try:
        e = next(generator)
        print(e)
    except:
        print("没有更多的元素")
        break

# 定义生成器的方式二: 借助函数完成
# 只要函数中出现yield关键字, 说明函数就不是函数, 就变成生成器了
# 斐波那契数列
"""
步骤: 
1. 定义一个函数, 函数中使用yield关键字
2. 调用函数, 接受调用的结果
3. 得到的结果就是生成器
4. 借助next(), __next__()得到元素 

"""


# def func():
#     n = 0
#     while True:
#         n += 1
#         yield n  # 相似return n + 暂停
#
#
# g = func()
# print(next(g))
# print(next(g))


def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b  # return b + 暂停
        a, b = b, a+b
        n += 1
    return "没有更多元素!!!"  # return 就是在得到StopIteration的提示信息

g = fib(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

