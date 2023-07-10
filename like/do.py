name = input("请输入用户名:")
if name == "谢容容":
    print("身份验证成功")
    password = int(input("请输入密码:"))
    if password == 5201314:
        print("密码成功")
    else:
        print("密码失败")
else:
    print("身份验证失败")

