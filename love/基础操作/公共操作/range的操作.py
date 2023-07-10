# range(1, 5)可以直接转换成列表的形式
print(list(range(1, 5)))

# 也可以直接用*解包获得
print(*range(1, 5))

# 直接打印range(1, 5)
print(range(1, 5))  # range(1, 5)

# range(start, stop, [,step]
# range有三个参数,第一个为起始数值,第二个为结束数值,第三个为步长,相当于等差数列的公差
# 当start > stop时,返回为空
# 当step为负数时,生成的序列递减