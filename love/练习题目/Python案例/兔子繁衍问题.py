def rabbit(month_):
    number, new_number = 1, 1
    for i in range(month-1):
        number, new_number = new_number, number + new_number
    else:
        return f"到{month}月,会有{number}只"


if __name__ == '__main__':
    month = int(input("请输入月份:"))
    print(rabbit(month))
