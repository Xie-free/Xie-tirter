list1 = ["name", "ago", "gender"]
list2 = ["Xie", "16", "girl"]
# 如何快速合并字典
# 字典推导式作用:快速合并列表为字典或提取字典中目标数据
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)

dict1 = {list1[i]: list2[i]for i in range(len(list2))}
print(dict1)

# 总结：
# 1. 如果两个列表数据个数相同,len统计任何一个列表长度都可以
# 2. 如果两个列表数据个数不同,len统计数据多的列表个数会报错,len统计数据少的列表个数,不会报错

# 提取字典当中的目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 1. 需求：提取电脑台数大于200
# 获取所有键值对数据,判读value值大于等于200返回
print(counts.items())
dict2 = {key: value for key, value in counts.items() if value >= 200}
print(dict2)