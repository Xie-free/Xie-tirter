"""
格式化:
1. %d %s %f .....
    print("xx说:%s" % xxxx)
2. format
"""
name = "xxx"
age = 18

result = "{}今年{}岁".format(name, age)
print(result)

print("我叫{},今年{}岁".format("小明", 16))

# 填充的字符可以多余{}
print("我爱吃{}和{}".format("xx", "xx", "xx"))

# {}的字符不可以多余字符, 否则报错
# print("我爱吃{}和{}和{}".format("xx", "xx"))

# 使用数字填充,从0开始
result = "{0}今年{1}岁, 我也{1}岁".format(name, age)
print(result)

# 变量名的形式, format的参数必须是关键字参数
result = "{name}今年{age}岁, 我也{age}岁".format(name = "xxx", age = 16)
print(result)




