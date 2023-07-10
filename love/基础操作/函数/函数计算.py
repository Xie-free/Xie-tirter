# 1. 任意三个数的和
def san_shu(a, b, c):
    """ 函数的说明文档 """
    return (a+b+c)/3
help(san_shu)
a = int(input(f"请输入你的第一个值"))
b = int(input(f"请输入你的第二个值"))
c = int(input(f"请输入你的第一个值"))
he = san_shu(a, b, c)
print(int(he))


