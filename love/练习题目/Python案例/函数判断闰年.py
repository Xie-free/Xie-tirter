def leap_year(year):
    if len(str(year)) == 4:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return "Ture"
        else:
            return "False"
    else:
        return "请输入四位数年份"


# 打印返回结果
print(leap_year(int(input("请输入一个四位数年份:"))))
