name = "蔡徐坤"
age = 26

# 我喜欢欢看26岁的蔡徐坤打篮球
print("我喜欢看" + str(age) + "岁的" + name + "打篮球!")

# 字符串如何格式化
"""
  符号:
  %s 字符串   # string
  %d 整数     # digit
  %f 浮点数   # float  
"""
print("我喜欢听%d岁的%s打篮球!" % (age, name))

money = 999.97
print("%d岁的%s一场篮球挣了%.2f块钱" % (age, name, money))
print("%s岁的%s一场篮球挣了%s块钱" % (age, name, money))  # str(age)


