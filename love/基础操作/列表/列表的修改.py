name_list = ["123", "xiao", "xie", "567", "xiao", "deng"]
# 1. 指定修改下标的数据
name_list[0] = "like"  # 修改123为like
print(name_list)
name_list[3] = "love"
print(name_list)  # 修改567为love

# 1. insert():插队
a = [1, 4, 5, 6, 7, 9]
a.insert(1, 2)
print(a)  # [1, 2, 4, 5, 6, 7, 9]

# 2. 逆序 reverse()
list1 = ["deng", "xiao", "like", "xie", "xiao", "love"]
list1.reverse()
print(list1)  # ['love', 'xiao', 'xie', 'like', 'xiao', 'deng']

# 3. sort() 排序：升序 和 降序
list2 = [1, 5, 28, 19, 2]
list2.sort()
print(list2)  # [1, 2, 5, 19, 28], 升序排序
# 默认升序函数
list2.sort(reverse=False)
print(list2)  # [1, 2, 5, 19, 28], 说明False等于升序排序
list2.sort(reverse=True)
print(list2)  # [28, 19, 5, 2, 1], 说明True等于降序排序
