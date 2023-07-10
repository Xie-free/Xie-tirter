"""
得到生成器的方式
1. 通过列表推导式得到生成器

"""

# [x for x in range(10000)]

# [0, 3, 6, 9, 12, 15, 18, 21......]

new_list = [x*3 for x in range(10)]
print(new_list)
print(type(new_list))

# 得到生成器
generator = (x*3 for x in range(10))
print(generator)
print(type(generator))  # <class 'generator'>

# 方式一:通过调用__next__()  方式得到元素
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())

# 方式二: next(生成器对象)  # builtins 系统内置函数
# 每调用一次next则会产生一个元素
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator))  # StopIteration  生成器本来就可以产生10个, 得到10个, 在调用next(generator) 抛出异常
