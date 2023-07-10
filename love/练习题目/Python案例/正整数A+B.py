# 条件A和B必须是[1, 1000]之间的正整数,如果不是,则要在相应的位置修改成?符号
def decide(n):
    try:
        n = int(n)
        if 1 <= n <= 1000:
            return n
        else:
            n = "?"
            return n
    except ValueError:
        n = "?"
        return n


if __name__ == '__main__':
    ls = input("请输入两个正整数,用空格隔开").split(" ")
    if isinstance(decide(ls[0]), str) or isinstance(decide(ls[1]), str):
        print(f"{decide(ls[0])} + {decide(ls[1])} = ?")
    else:
        print(f"{decide(ls[0])} + {decide(ls[1])} = {decide(ls[0]) + decide(ls[1])}")
