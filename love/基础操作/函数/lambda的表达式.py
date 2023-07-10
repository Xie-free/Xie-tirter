# 需求:函数 返回值100
# 1. 函数
def cat():
    return 100


print(cat())

# 2. lambda  匿名函数
# lambda 参数列表:表达式
cat2 = lambda: 100
print(cat2)  # lambda内存地址
print(cat2())
