# in 判读为元素是否存在
# not in 判读元素是否不存在
str1 = "a"
list1 = ["jie"]
t1 = ("world",)
dict1 = {"name": "jie"}
print("a" in str1)
print("a" not in str1)

print("jie" in list1)
print("jie" not in list1)

print("world" in t1)
print("world" not in t1)

print("name" in dict1)
print("name" not in dict1)
print("name" in dict1.keys())
print("name" in dict1.values())

print("jie" in dict1)
print("jie" in dict1.values())
print("jie" not in dict1)
print("jie" not in dict1.keys())
