dict1 = {"name": "Yu", "ago": "16", "gender": "男"}
# del 删除字典或指定的键值对
# del(dict1)
# print(dict1) 报错

del dict1["name"]
print(dict1)  # {'ago': '16', 'gender': '男'}
# del dict1["names"]
# print(dict1) 报错

# clear
dict1.clear()
print(dict1)  # {}