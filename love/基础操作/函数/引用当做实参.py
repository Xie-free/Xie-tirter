# 需求:引用是否可以当实参
"""
1. 定义函数：有形参
  1.1 访问打印形参看是否有数据
  1.2 访问形参的id
  1.3 改变新参的数据,查看这个形参并打印id,看id是否相同
2.调用函数 ---- 把可变和不可变两种类型依次当做实参去传入
"""


def test1(a):
    print(a)
    print(id(a))

    if type(a) == list:
        a.append(f)
        print(a)
        print(id(a))
    elif type(a) == int:
        a *= d
        print(a)
        print(id(a))


d = int(input(f"乘数"))
b = int(input(f"请输入您的数，它会乘{d}"))
test1(b)

f = list(input(f"请输入您要往列表里面添加的数据："))
c = []
test1(f)
