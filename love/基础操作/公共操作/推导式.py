# 集合推导式  {}  类似于列表推导式, 在列表推导式的基础上添加一个去除重复项
list1 = [1, 3, 4, 5, 6, 7, 7, 8, 1, 1, 1, ]

set1 = {x for x in list1}
print(set1)

set2 = {i+1 for i in list1}
print(set2)

set3 = {i+1 for i in list1 if i> 5}
print(set3)

dict1 = {"a": "A", "b": "B", "c": "C", "d": "C"}

new_dict = {value: key for key, value in dict1.items()}
print(new_dict)