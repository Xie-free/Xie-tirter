# 需求：任意两个数字按照指定要求整理后再进行计算
# 1. 写法一
def add_num(a, b):
    # 绝对值
    return abs(a) + abs(b)


result = add_num(-10, 80)
print(result)

# 2. 方法二:高阶函数:f是第三个参数,用来接受函数用的
def sum_num(a, b, c):
    return c(a) + c(b)


result1 = sum_num(-40, -5.8, abs)
print(result1)

result2 = sum_num(-0.9, 45.5, round)
print(result2)