set1 = {1, 5, 6, 7, 8, 9, 10}
set2 = {1, 66, 22, 8, 9, 10}

# 集合: 交集 intersection 并集 union  差集difference

result = set1.intersection(set2)  # &  交集
print(result)
print(set1 & set2)

result1 = set1.union(set2)  # |  并集
print(result1)
print(set1 | set2)

# set1.difference(set2)  返回值为{5, 6, 7}
result2 = set1.difference(set2)  # -  差集
print(result2)
print(set1 - set2)

# set2.difference(set1)  返回值为{66, 22}
result3 = set2.difference(set1)  # - 减号分前后
print(result3)
print(set2 - set1)
