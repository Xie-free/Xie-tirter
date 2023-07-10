# 元组的功能跟列表一样，但他里面的数据不能修改
t1 = (1, 10, 11, 15)
print(t1)

print(type(t1))  # <class 'tuple'>
# 如单个元组数据,要加逗号,不然数据类型为（）里面的类型
t2 = (10)
print(type(t2))  # <class 'int'>

t3 = (10,)
print(type(t3))  # <class 'tuple'>

t4 = ("xiao")  # <class 'str'>
print(type(t4))

t5 = ("xiao",)
print(type(t5))  # <class 'tuple'>

# 元组的数据不支持修改,只支持查找
# 元组函数跟列表函数一样
tuple1 = ("xiao", "xie", "xiao", "deng")
print(tuple1[0])  # xiao

print(tuple1.index("xiao"))  # 0

print(tuple1.count("xie"))  # 1

print((len(tuple1)))  # 4
