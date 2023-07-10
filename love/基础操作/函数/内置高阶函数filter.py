# filter(func, lis) 函数用来过滤掉不符合条件的元素,返回一个filter 对象.如果要转换为列表,可以使用list()来转换
"""
    1. 定义功能函数：过滤序列中的偶数
    2.调用filter
"""
lis = [1, 31, 1050, 1021, 19099, 5076, 78654, 3]


def func(x):
    return (x+1) % 2 == 0


result = filter(func, lis)

print(result)

print(list(result))