# 输入两个整数
int_1 = eval(input("请输入第一个整数"))
int_2 = eval(input("请输入第二个整数"))
# 计算和、差、积、商
if type(int_1) and type(int_2) == int:
    print(f"{int_1} + {int_2} = {int_1 + int_2}")
    print(f"{int_1} - {int_2} = {int_1 - int_2}")
    print(f"{int_1} * {int_2} = {int_1 * int_2}")
    if int_1 != 0:
        print(f"{int_1} / {int_2} = {int(int_1 / int_2)}")
    else:
        print("除数不能为零")
else:
    print("请输入两个整数")
