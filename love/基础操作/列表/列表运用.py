name_list = ["Tom", "Lily", "Rose"]
print(name_list)      # Tom, Lily, Rose
# 查找必须是[],小括号要报错
print(name_list[0])   # Tom
print(name_list[1])   # Lily
print(name_list[2])   # Rose
# index():返回指定数据所在位置的下标
# *不存在就报错
# print(name_list.index("Toms"))   # 报错
print(name_list.index("Tom"))   # 0
# count():统计指定数字在当前列表中出现的次数
print(name_list.count("Toms"))  # 0
print(name_list.count("Tom"))   # 1
# len():访问列表长度，即列表中数据的个数
print(len(name_list))  # 3
name_list1 = ["like", "黑", "姬", "结", "灯", ]
print(len(name_list1))  # 5
name_list2 = "".join(name_list1)
print(name_list2)
