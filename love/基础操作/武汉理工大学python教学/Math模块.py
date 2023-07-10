import math

# 导入math模块, 引用函数名前要加'Math'.
print(math.pi)  # pi为圆周率常量: 3.141592653589793

# math.factorial(x): 返回x的阶乘
print(math.factorial(6))  # 720
# 要求x为非负整数, x为负数或浮点数时返回错误
# print(math.factorial(-6))
# print(math.factorial(6.5))

# math.fsum(): 返回浮点数迭代求和的精确值
list_number = []
i = 1
while i <= 10:
    list_number.append(0.1)
    i += 1
print(list_number)
print(math.fsum(list_number))  # 1.0
print(sum(list_number))  # 0.9999999999999999

# math.gcd(*integers): 返回给定的整数参数的最大公约数
print(math.gcd(88, 44, 22))  # 22
# 返回值是能同时整除所有参数的最大正整数
print(math.gcd(88, 44, 0))  # 44
# 如果所有参数为零或无参数, 则返回值为零
print(math.gcd(0, 0))  # 0

# math.lcm(*integers): 返回给定的整数参数的最小公倍数
print(math.lcm(5, 44, 22))  # 220
# 如果参数之一为0, 返回值为0
print(math.lcm(22, 44, 0))  # 0
# 无参数时, 返回值为1
print(math.lcm())

# math.floor(x): 返回不大于x的最大整数
print(math.floor(9.99))  # 9

# math.ceil(x): 返回不小于x的最小整数
print(math.ceil(9.01))  # 10

# math.sqrt(x): 返回非负整数x的平方根
print(math.sqrt(5))  # 2.23606797749979

# math.isqrt(x): 返回非负整数x的整数平方根
print(math.isqrt(5))  # 2
