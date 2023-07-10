# del 目标 或 del(数据）
new_list = ["xiao", "xie", '"xiao"', "deng"]
del new_list  # 或 del (new_list)
# print(new_list)  # name 'new_list' is not defined

new_list1 = ["xiao", "xie", '"xiao"', "deng", "jie"]
print(new_list1)  # ["xiao", "xie", '"xiao"', "deng", "jie"]
# del 可以删除指定下标的数据
del new_list1[4]
print(new_list1)  # ['xiao', 'xie', '"xiao"', 'deng']

# pop() -- 删除指定下标的数据，如果不指定下标，默认删除最后一个数据
# 无论是按照下标还是删除最后一个,pop函数都会返回这个被删除的数据
a = new_list1.pop()
# 因为pop会返回列表的数据，所以要设个变量
print(a)  # deng
print(new_list1)  # ['xiao', 'xie', '"xiao"']

b = new_list1.pop(2)
print(new_list1)  # ['xiao', 'xie']

# remove(数据）
new_list1.remove("xiao")
print(new_list1)  # ['xie']

# clear() -- 清空
new_list1.clear()
print(new_list1)  # []