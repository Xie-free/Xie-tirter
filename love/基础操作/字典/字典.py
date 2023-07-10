# 字典的特点：
#   符号为大括号
#   数据为键值对形式出现
#   各个键值对之间用逗号隔开
# 1 . 有数据的字典：name的值Yu, ago的值为16, gender的值是男
dict1 = {"name": "Yu", "ago": "16", "gender": "男"}
print(dict1)  # {'name': 'Yu', 'ago': '16', 'gender': '男'}
print(dict1["name"])  # Yu
print(type(dict1))  # <class 'dict'>

# 2 . 空字典
dict2 = {}
print(type(dict2))  # <class 'dict'>

dict3 = dict()
print(type(dict3))  # <class 'dict'>

print(dict1)  # {'name': 'Yu', 'ago': '16', 'gender': '男'}
