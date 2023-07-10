a = int(input("有钱请输入1"))

if a == 1:
    print("有钱请上车")
    b = input("是否有座位，有输入1")
    if b == "1":
        print("有座位，请坐")
    else:
        print("无座位，请站着")
else:
    print("没钱不能上车")
