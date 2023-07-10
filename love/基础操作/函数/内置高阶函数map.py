# map()
# map(func, list) 将传入的函数变量func作用到list变量的每个元素中
"""
  1 . 准备列表数据
  2 . 准备二次方计算函数
  3 . 调用map
  4 . 验收成果
"""
lis = [1, 5, 10, 15, 18]
list1 = []

def func(x):
    return x ** 2


result = map(func, lis)

print(result)

print(list(result))


for i in range(5):
    a = lis[i] ** 2
    list1.append(a)

print(list1)
