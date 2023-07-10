def rabbit_chick(head, foot):
    for r in range(1, head):
        for c in range(1, head):
            if (r * 4) + (c * 2) == foot and r+c == head:
                return f"有{c}只鸡, {r}只兔子"
    else:
        return "Data Error!"


if __name__ == '__main__':
    head_sum, foot_sum = map(int, input("请输入头数和腿数(空格隔开):").split())
    print(rabbit_chick(head_sum, foot_sum))
