# abs(x): 绝对值函数
# x为整数或浮点数时返回其绝对值
# x为复数时返回复数的模
print(abs(-3))  # 3
print(abs(-3.5))  # 3.5
print(abs(3 + 4j))  # 5.0

# pow(x,y): 幂函数
# 返回x的y幂
print(pow(2, 3))  # 8
print(pow(2, 8))  # 256
print(pow(2, 1 / 2))  # 1.4142135623730951

# pow(x,y,z): X的y次幂计算结果再对z取模,效率高
print(pow(2, 3, 3))  # 2

# max(arg1, arg2,.....): 最大值函数
# 从多个参数中返回其最大值
print(max(1, 2, 3, 4, 5, 6, 7))  # 7

# min(arg1, arg2,...): 最小值函数
# 同上
print(min(1, 2, 3, 4, 5, 6, 7))  # 1

# sum(iterable): 求和函数
# 将元素为数值的可迭对象中的元素累加
print(sum(range(11)))  # 55

# sum(iterable, start=0): 求和函数
# 将元素为数值的可迭对象中的元素累加到start上
print(sum(range(11), start=10))  # 65

# round(number, n): 浮点数number保留n位小数的最短表示
# 多数浮点数无法精确转为二进制, 会导致部分数字取舍与期望不符
print(round(3.1425, 3))  # 3.143

# 当小数部分的末位为0或n超过小数位时,返回该数的最短表示
print(round(3.0000, 2))  # 3.0
# 当n省略时,将number转换为最接近的整数
# 四舍六入五考虑:
# 五后为零就进一
# 五前为偶应舍去
print(round(3.1415926, 3))  # 3.142
print(round(3.5))  # 4
print(round(3.4))  # 3


