# 分别输入三个浮点数
a = float(input("请输入a的长度"))
b = float(input("请输入b的长度"))
c = float(input("请输入c的长度"))

# 输出周长和面积
C = a + b + c
S = (a + b + c) / 2
area = (S * (S - a) * (S - b) * (S - c)) * 0.5
# 获取三条边的最大数
max_number = max(a, b, c)
# 判断最短的两条边之和是否大于第三边
if a+b+c > max_number * 2:
    print(f"三角形的周长为:{round(C, 2)}")
    print(f"三角形的面积为:{round(area, 2)}")
else:
    print("三条边无法构成三角形")
