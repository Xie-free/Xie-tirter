# 引入math库
import math

# 输入AB和CD的长度
AB = eval(input("请输入线段AB的长度"))
CD = eval(input("请输入线段CD的长度"))
# AD等于0.5AB
AD = AB / 2
# 求半径OA
OA = (AD ** 2 + CD ** 2) / (CD * 2)
# 圆心角
AOB = 2 * math.asin(AD / OA)
# 扇形AOB的面积
area_of_sector = AOB / (2 * math.pi) * math.pi * (OA ** 2)
# 三角形的面积
area_of_triangle = 1 / 2 * (OA ** 2) * math.sin(AOB)
# 弓形面积为扇形面积减去三角形面积
area_of_arch = area_of_sector - area_of_triangle
print(round(OA, 2))
print(round(area_of_arch, 2))