import math

r = 6371 * 1000
S = 4 * math.pi * r ** 2
V = (4 * math.pi * r ** 3) / 3
L = 2 * math.pi * r
print(f"地球表面积为{S:.2f}平方米", f"体积为{V:.2f}立方米", f"周长为{L:.2f}米", sep="\n")
new_r = (L + 1) / (2 * math.pi)
space = new_r - r
print(f"空隙为{space:.2f }米")
if space > 0.1:
    print("可以")
else:
    print("不可以")
