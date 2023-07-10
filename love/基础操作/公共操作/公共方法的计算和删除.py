# len():计算容器中元素的个数
str1 = "a"
list1 = ["jie"]
t1 = ("world",)
s1 = {10, 20, 50, 90, 5}
dict1 = {"name": "jie"}
print(len(str1))
print(len(list1))
print(len(t1))
print(len(s1))
print(len(dict1))

# del或del():删除
# del str1
# print(str1)

# del list1
# print(list1)

# del s1
# print(s1)

# del dict1
# print(dict1)
del dict1["name"]
print(dict1)