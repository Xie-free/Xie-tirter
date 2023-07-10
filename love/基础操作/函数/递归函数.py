"""
如果一个函数在内部不调用其它的函数, 而是自己本身的话, 这个函数就是递归函数
遵循:
1. 必须要有出口
2. 每次递归向出口靠近

"""


# def test():
#     print("-----test-----")
#
#
# def a():
#     print("------a------")
#     # 调用a函数
#     a()
#
#
# a()

# 1 - 10 打印  数字
# def test(i):
#     if i == 10:
#         print("10")
#     else:
#         print(i)
#         i += 1
#         test(i)
#
#
# test(1)


# 1- 10 累加和
def test1(i):
    if i == 10:
        return 10
    else:
        return i + test1(i + 1)


r = test1(1)
print(r)


# 5！ = 1*2*3*4*5
def test2(i):
    if i == 5:
        return 5
    else:
        return i * test2(i + 1)


b = test2(1)
print(b)


# 使用递归实现斐波那契数列
def test3(a, c):
    if 1 <= a <= 1000 and 1 <= c <= 1000:
        a, c = a + c, c
        return test3(a, c)


print(test3(1, 1))
