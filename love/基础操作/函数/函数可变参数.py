"""
可变参数:
*args
**kwargs

拆包和装包
函数装包:
def 函数(*+名字,最好是args好理解):    ---->此时会出现装包操作
    pass
函数(1,2,3,4)

拆包:
list, tuple,set
调用的时候:
函数(*list)  |  函数(*tuple)  |  函数名(*set)
拆包过程
"""


# 求和
# def get_sum(a, b):
#     r = a + b
#     print(r)


def get_sum(*args):
    print(args)
    s = 0
    for i in args:
        s += i
    print("和:", s)


"""
装包                          拆包
a, *b, c = 1, 2, 3, 4, 5      a, b, c = (1, 2, 3)
print(a)  # 1                 print(a)  # 1
print(b)  # [2, 3, 4]         print(b)  # 2
print(c)  # 5                 print(c)  # 3

"""

get_sum(1, 2, 3, 4, 5, 6)
get_sum(1, 1, 1, 1, 1, 1, 1)
get_sum()

random_int = [123, 4534, 123, 3234, 9087, 954]
get_sum(*random_int)