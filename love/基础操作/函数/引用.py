# 可变和不可变

# 1. int类型不可变
# 1.1 声明变量保存整形数据,把这个数据赋值到另一个变量： id()检测两个变量的id值( 内存的十进制值)
a = 1
b = a
print(b)

# 发现a和b的id值是相同的
print(id(a))
print(id(b))

# 修改a的数据测试id值
a = 2

print(b)

# 因为修改了a的数据, 内存要开辟另外一份内存去存储2.id的检测a和b的地址不同了
print(id(a))

print(id(b))

# 2. 列表类型可变
aa = [10, 50]
bb = aa

print(bb)

print(id(aa))
print(id(bb))

aa.append(40)
print(aa)
print(bb)  # 列表是可变类型

print(id(bb))
print(id(aa))