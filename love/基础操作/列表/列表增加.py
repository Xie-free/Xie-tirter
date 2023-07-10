# append:列表结尾追加数据
# 列表序列.append(数据)
new_list = ["Tom", "Lily", "Rose"]
new_list.append("xiao xie")
print(new_list)  # ['Tom', 'Lily', 'Rose', 'xiao xie']

# append函数追加数据的时候如果数据是一个序列，追加整个序列到列表结尾
new_list.append(["xiao xie"])
print(new_list)  # ['Tom', 'Lily', 'Rose', 'xiao xie', ['xiao xie']]

# extend():列表结尾追加数据, 如果数据是一个序列,则将这个序列的数据逐一添加到列表
# 列表数据.extend(数据）
new_list.extend("xiao xie")
print(new_list)  # ['Tom', 'Lily', 'Rose', 'xiao xie', ['xiao xie'], 'x', 'i', 'a', 'o', ' ', 'x', 'i', 'e']

# extend打印列表会把列表的括号去掉
new_list.extend(["xiao xie"])
print(new_list)  # ['Tom', 'Lily', 'Rose', 'xiao xie', ['xiao xie'], 'x', 'i', 'a', 'o', ' ', 'x', 'i', 'e', 'xiao xie']

# insert():指定位置新增数据
# 列表序列。insert(位置下标,数据）
new_list1 = ["xiao", "xie"]
new_list1.insert(1, "deng")
print(new_list1)  # ['xiao', 'deng', 'xie']

new_list1.insert(2, "xiao")
print(new_list1)  # ['xiao', 'deng', 'xiao', 'xie']
