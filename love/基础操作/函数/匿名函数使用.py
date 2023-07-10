# 匿名函数: 简化函数定义
# 格式: lambda  参数1,  参数2.....: 运算

# def func():
#     print("aaa")
#
#
# def add(a, b):
#     s = a + b
#     return s

s = lambda a, b: a + b
print(s)  # s 就是函数function

result = s(2, 3)
print(result)


# 匿名函数作为参数
def func(x, y, func):
    print(x, y)
    print(func)
    s = func(x, y)
    print(s)


# 调用func
func(4, 5, lambda a, b: a + b)

list1 = [3, 5, 6, 7, 12, 998]

m = max(list1)

print("列表最大值:", m)

list2 = [{"a": 10, "b": 20}, {"a": 14, "b": 27}, {"a": 19, "b": 29}]

m = max(list2, key=lambda x: x["a"])
print("列表的最大值:", m)
