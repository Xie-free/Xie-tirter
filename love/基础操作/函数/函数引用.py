"""
引用:
1. 不是在函数中使用, 可以通过sys.getrefcount(a)引用次数
    del 变量        表示删除了一个引用
2. 函数的引用:
    必须要分清楚传递的值是可变类型还是不可变类型.
    如果是可变,里面发生改变,外层就能看到改变后的内容
    如果是不可变,里面发生改变,不会影响外部得到的变量值



"""

a = 10
b = a
c = a

print(id(a))
print(id(b))
print(id(c))

import sys

print(sys.getrefcount(a))

list1 = [1, 2, 3, 4, 5]
list2 = list1  # list1将其引用地址给list2赋值
list3 = list2
print(sys.getrefcount(list1))  # 计数list1地址的被引用次数, 本身算一次

del list3
print(sys.getrefcount(list1))

del list1
print(sys.getrefcount(list2))


def test(n1):  # n 是一个数值
    for i in range(n1):
        print("----->", i)

        n1 += 1


n = 9
test(n)

print(n)

print("-" * 100)


def list1(l):
    if isinstance(l, list):
        for i in l:
            print("---->", i)
        l.insert(0, 8)
    else:
        print("不是列表类型")


list1(list2)
print(list2)
