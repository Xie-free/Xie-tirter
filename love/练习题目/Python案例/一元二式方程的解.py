a = eval(input("请输入a的数值:"))
b = eval(input("请输入b的数值:"))
c = eval(input("请输入c的数值:"))
result = (b ** 2) - (4 * a * c)
x_1 = (-b + pow((b ** 2) - 4 * a * c, 1 / 2)) / (2 * a)
x_2 = (-b - pow((b ** 2) - 4 * a * c, 1 / 2)) / (2 * a)
if a == 0:
    if result >= 0:
        print(result)
elif a == 0 and b == 0:
    print("Data error!")
elif result < 0:
    print("方程无实数解")
elif x_1 == x_2:
    print(round(x_1, 2))
else:
    if x_1 > x_2:
        print(f"{x_1:.2f}, {x_2:.2f}")
    else:
        print(f"{x_2:.2f}, {x_1:.2f}")


