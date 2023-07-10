# 打印地址
print(r"D:\users\tasks\mytask.exe")

# 打印信息表
name = input("请输入姓名:")
sex = input("请输入性别:")
ago = int(input("请输入年龄:"))
height = eval(input("请输入身高:"))
weight = eval(input("请输入体重:"))
blood = eval(input("请输入血氧指数:"))
print("《个人基本信息汇总表》", f"姓名:{name}", f"性别:{sex}", f"年龄:{ago}",
      f"身高:{height}", f"体重:{weight}", f"血氧指数:{blood}", sep="\n")
