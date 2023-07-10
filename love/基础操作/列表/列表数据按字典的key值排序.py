student = [
    {"name": "Xie", "age": 16},
    {"name": "Jie", "age": 17},
    {"name": "Yu", "age": 18}
]

# sort(key= lambda.....,reverse = bool数据)
# 1 . name key 对应的值进行升序排序
student.sort(key=lambda x: x["name"])
print(student)

# 2 . name key 对应的值进行降序排序
student.sort(key=lambda x: x["name"], reverse=True)
print(student)

# 3. age key 对应的值进行升序排序
student.sort(key=lambda x: x["age"])

