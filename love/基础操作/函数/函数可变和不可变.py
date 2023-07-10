"""
可变与不可变:
不可变: 当改变变量的值时, 地址发生了改变.
    类型: int   str   float   bool   tuple
可变类型: 里面的内容发生了改变, 但是地址没有发生改变
    类型: list   dict   set
"""
a = 100
print(id(a))  # 140734766554488
a = 90
print(id(a))  # 140734766554168

s = "abc"
print(id(s))  # 2544790758384
s = "cyx"
print(id(s))  # 2544790758320

t1 = (1, 2, 3, 4)  # 2188207460880
print(id(t1))

t1 = (1, 2, 3, 4, 5)  # 2188207251888
print(id(t1))

l1 = [1, 2, 3]
print(id(l1))

l1.append(4)
print(id(l1))
