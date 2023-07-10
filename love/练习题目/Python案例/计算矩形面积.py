# 用户输入长和宽
Length = eval(input("请输入矩形的长"))  # eval函数将字符串转换成数值
Width = eval(input("请输入矩形的宽"))
area = Length * Width  # 长和宽相乘得面积
print(round(area, 2))

