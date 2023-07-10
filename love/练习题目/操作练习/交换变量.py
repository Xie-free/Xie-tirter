# 1.方法一
"""
1.1 定义中间的第三变量, 为了临时存储a或b 的数据
1.2 把a的数据存储c,做保存
1.3 把b的数据赋值到a， a = 20
1.4 把c数据赋值到b，b = 10
"""
# 借助第三变量存储数据
a = 10
b = 20
c = 0
c = a
print(a)  # 10
print(c)  # 10
a = b
print(a)  # 20

b = c
print(b)  # 10

# 2.方法二
a, b = 1, 2
a, b = b, a
print(a)  # 2
print(b)  # 1
