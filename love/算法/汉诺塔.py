x = 0


def Hanoi_Tower(n, a, b, c):  # 定义一个函数, 参数n为盘子数, abc分别为a柱,b柱,c柱
    if n > 0:  # 结束条件
        Hanoi_Tower(n - 1, a, c, b)
        global x
        x += 1
        print(f"从{a}移动到{c}")
        Hanoi_Tower(n - 1, b, c, a)
        print(f"{x}步")


n = int(input("请输入多少个盘子:"))
Hanoi_Tower(n, "A柱", "B柱", "C柱")
