def palindromic(m):
    number = 0  # 定义次数
    for i in range(1, 9):  # 遍历
        reverse = str(m)[::-1]  # 取反
        lis = [reverse, m]  # 加列表
        reverse, m = map(int, lis)  # 转类型
        if reverse == m:  # 判断
            return number
        m = m + reverse  # 相加
        number += 1

    else:
        return 0


if __name__ == '__main__':
    m_ = input("请输入一个整数")
    print(palindromic(m_))
