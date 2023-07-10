import math
# 12寸的披萨和两个七寸的披萨
Pai = math.pi  # 常量用大写字母
m = eval(input("请输入原有尺寸"))
n = eval(input("请输入更换尺寸"))
result = (Pai * (m / 2) ** 2) / (Pai * (n / 2) ** 2)
print(math.ceil(result))