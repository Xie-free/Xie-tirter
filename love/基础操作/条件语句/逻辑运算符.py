"""
逻辑运算符:
and or not

结果:
and: 与  并且
A and B
True and True  ----> True
True and False  ----> False
False and True  ----> False
False and False  ----> False

or : 或  或者   只要有一侧为真True, 结果就为True

A or b
True and True  ----> True
True and False  ----> True
False and True  ----> True
False and False  ----> False

not:

not True  ----> False
not False ----> True

"""

a = 1
b = 3

# and 两边都是非0 数字,结果是最后的数字值
print(a and b)  # 3
print(b and a)  # 1

c = 0
# and 两边只要有一边为0,结果即为0
print(c and a)  # 0
print(a and c)  # 0

print(a > c and a < b)  # True    #username == "xiaohua" and password == "123456    "
print(a == c and a < b)  # False

print("*" * 20)

print(b or a)  # 3
print(a or b)  # 1

print(c or a)  # 1
print(c or b)  # 3
print(a or c)  # 1

print(a > c or a < b)  # True
print(a == c or a < b)  # True  # 场景: 1. 账号密码  2. 手机号码  验证码
# 账号名/手机号码 + 密码

print("*" * 20)
flag = True
print(not flag)  # False

print(not a>c)  # False
