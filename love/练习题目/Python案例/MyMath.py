def power(x, n):  # 接受一个x和n的参数,返回x的n次方结果的浮点数
    """
    :param x: x为输入整数
    :param n: n为x的次方
    :return: 返回x的n次方结果
    """
    if x <= 0 and isinstance(int, n):  # 判断x是否大于零和n是否为一个整数
        return ValueError
    elif x == 0 and n == 0:
        return 1.0
    else:
        result = 1.0
        for i in range(n):
            result *= i
        else:
            return result  # 返回结果


def gcd(*args):
    """
    :param args: 输入任意整数
    :return: 返回整数的最大公因数
    """
    number_lis = []  # 创建空列表
    for i in args:  # 遍历获取输入的整数
        for num in range(2, i + 1):
            if i % num == 0:
                number_lis.append(num)
    else:
        dict_empty = {}
        for a in number_lis:
            if f"{a}" not in dict_empty:
                dict_empty[f"{a}"] = 1
            else:
                dict_empty[f"{a}"] += 1
        else:
            result_list = []
            judgement_number = sorted(dict_empty.items(), key=lambda v: v[1])
            for c in range(1, len(dict_empty) + 1):
                if (judgement_number[-1 * c])[1] == len(args):
                    result_list.append(judgement_number[-1 * c])
            else:
                for i in result_list:
                    return int(i[0])


def lcm(*args):
    """
    :param args: 输入任意整数
    :return:  返回整数的最小公倍数
    """
    if len(args) == 2:
        num = 1  # 设置变量
        for i in args:  # 获取元素
            num *= i
        else:
            result_gcd = gcd(*args)
            result = num / result_gcd
    else:
        return "不会"


def copy_sign(x, y):
    """
    :param x: 传入的值为整数
    :param y: 传入的为整数,关键是符号
    :return:  返回第一个参数的值和第二个参数的符号
    """
    if x > 0 and y > 0:  # 判断
        return x
    elif x < 0 and y > 0:
        return x * -1
    elif x > 0 and y < 0:
        return x * -1
    elif x < 0 and y < 0:
        return x


def ceil(x):
    """
    :param x: # 输入一个整数
    :return:
    """
    if x < 0:
        num = str(x).split(".")  # 切割字符串,从.号开始
        return int(num[0]) - 1
    else:
        num = str(x).split(".")
        return int(num[0])


def floor(x):
    """
    :param x: 输入一个整数
    :return:  返回向下取整
    """
    if x < 0:
        num = str(x).split(".")
        return int(num[0])
    else:
        num = str(x).split(".")
        if int(num[0]) == x:
            return int(num[0])
        return int(num[0]) + 1


def factorial(x):
    """
    :param x: 输入一个整数
    :return: 返回这个整数的阶乘
    """
    num = 1  # 设置初始值
    for i in range(1, x + 1):  # 遍历获取1到x的数,然后依次相乘
        num *= i
    return num

