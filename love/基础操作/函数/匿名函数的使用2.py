# map():
list1 = [1, 2, 7, 8, 8, 9, 45, 23, 42, 34]

result = map(lambda x: x + 2, list1)
print(list(result))

# for index, i in enumerate(list1):
#     list1[index] = i+2
#
# print(list1)

numbers_two = lambda x: x if x % 2 == 0 else x + 1

result1 = numbers_two(5)
print(result1)

# 对列表中的奇数进行加1操作
result = map(lambda x: x if x % 2 == 0 else x + 1, list1)

print(list(result))

# for index, i in enumerate(list1):
#     if i % 2 != 0:
#         list1[index] = i + 1
#
# print(list1)

# reduce(): 对列表中的元素进行加减乘除运算的函数
from functools import reduce

tuple1 = (3, 4, 10, 6, 8, 9)

result = reduce(lambda x, y: x + y, tuple1)

print(result)

tuple2 = (11,)

result = reduce(lambda x, y: x + y, tuple2, 10)

print(result)

# 动手测试减法
list2 = [122, 74, 58, 8, 9, 45, 23, 42, 34]
# result = (lambda x: x > 10, list2)
# print(result)
result = filter(lambda x: x > 10, list2)
print(list(result))

list3 = []

# def func(list2):
#     for i in list2:
#         if i > 10:
#             list3.append(i)
#         return list3

students = [{"name": "tom", "age": 19},
            {"name": "lucky", "age": 29},
            {"name": "live", "age": 16},
            {"name": "Alice", "age": 26},
            {"name": "lucky", "age": 24}]

# 找出所有年龄大于20岁的学生
result = filter(lambda x: x["age"] > 20, students)
print(list(result))

# 按照年龄从小到大

students = sorted(students, key=lambda x: x["age"])  # 升序
# students = sorted(students, key=lambda x: x["age"], reverse=True)  # 降序

print(students)

"""
max()
min()
sorted()

map():
reduce()
filter()
"""