# 元组内的列表可修改
tuple1 = ("xiao", "xie", "xiao", "deng")
tuple1[0]
tuple1 = ("xiao", "xie", ["xiao", "deng"])
print(tuple1[2])
print(tuple1[2][1])
tuple1[2][1] = "jie"
print(tuple1)
