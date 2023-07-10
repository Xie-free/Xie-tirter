# 输出年月份
year = input("请输入年份")
month = input("请输入月份")
day = input("请输入天数")

# 分割要求为空格
# 格式: 2022 09 16
print(year, month, day)

# 分割要求为-
# 格式: 2020-09-16
print(year, month, day, sep="-")

# 分割要求为/
# 格式: 2020/09/16
print(year, month, day, sep="/")

# 输出月日年
# 分割要求为，
# 格式: 09，16，2020
print(month, day, year, sep="，")

# 用str.format()格式输出
# 格式: 2020年09月16日
print("{}年{}月{}日".format(year, month, day))

# 用字符串拼接方法输出
# 格式: 2020年09月16日
print(year + "年"+month + "月"+day + "日")
