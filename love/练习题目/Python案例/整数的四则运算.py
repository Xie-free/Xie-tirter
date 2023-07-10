# 1.输入两个非零整数, 在四行中按顺序输出两个数的加、减、乘、除的计算结果.
num_1 = int(input("请输入第一个非零整数"))
num_2 = int(input("请输入第二个非零整数"))
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)

# 2.输入两个非零整数, 在四行中按顺序输出两个数的加、减、乘、除的计算结果.
# 要求输出与示例格式相同,符号前后各有一个空格.
# 例如
# 1 + 2 = 3
print(f"{num_1} + {num_2} = {num_1 + num_2}")
print(f"{num_1} - {num_2} = {num_1 - num_2}")
print(f"{num_1} * {num_2} = {num_1 * num_2}")
print(f"{num_1} / {num_2} = {num_1 / num_2}")

# 3.输出两个非零浮点数, 在四行中按顺序输出两个数的加、减、乘、除的计算式和计算结果.
# 计算结果str.format()方法保留小数点后三位数字.
# 要求输出与示例格式相同, 符号前后各有一个空格.
# 例如
# 2.66 + 3.1415926 = 5.802
float_1 = float(input("请输入第一个非零浮点数"))
float_2 = float(input("请输入第二个非零浮点数"))
print("{} + {} = {:.3f}".format(float_1, float_2, float_1 + float_2))
print("{} - {} = {:.3f}".format(float_1, float_2, float_1 - float_2))
print("{} * {} = {:.3f}".format(float_1, float_2, float_1 * float_2))
print("{} / {} = {:.3f}".format(float_1, float_2, float_1 / float_2))
# eval函数:
# eval(参数) 函数用来执行一个字符串表达式，并返回表达式的值
for i in "+-*/":
    # eval只能把字符串转换成表达式
    # 所以要把float_1和float_2转换成字符串之后再进行eval的使用
    print("{} {} {} = {:.3f}".format(float_1, i, float_2, eval(str(float_1)+i+str(float_2))))
