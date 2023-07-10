# 1. key值查找
dict1 = {"name": "Yu", "ago": "16", "gender": "男"}
print(dict1["name"])  # Yu
# print(dict1["id"]  # 报错
# 如果当前查找的key存在,则返回对应的值;否则则报错。

# 2. get
# 字典序列.get(key,默认值）
# 注：如果当前查找的key不存在则返回第二个参数（默认值）,如果省略第二个参数，则返回None
print(dict1.get("name"))  # Yu
print(dict1.get("id", 5))  # 5
print(dict1.get("id"))  # None

# 3. keys() 查找字典中的所有key，返回可迭代对象
print(dict1.keys())  # dict_keys(['name', 'ago', 'gender'])

# 4. values() 查找字典中所有的values,返回可迭代对象
print(dict1.values())  # dict_values(['Yu', '16', '男'])

# 5. items() 查找字典中所有的键值对，返回可迭代对象, 里面的数据是元组,元组数据1是字典key,元组数据2是字典key对应的值
print(dict1.items())  # dict_items([('name', 'Yu'), ('ago', '16'), ('gender', '男')])
