"""
以变量名:a
    str --->  int     int(a)   但是如果"9.9"而且是字符串类型转换成int的时候报错了
    str --->  float   float(a)

    int ---> str      str(a)
    float ---> str    str(a)
    int ---> float    float(a)
    float ---> int    int(a)   只不过float类型中小数点后面的数字被抹掉了
"""

flag = False
# bool ---> int    True ---> 1   False ---> 0
print(int(flag))

print(float(flag))

print(str(flag))  # "True"

a = 5  # 变量的值是:0, ""(空字符串), 转换结果是False, 其他只要变量有值则为True
print(bool(a))

a = 6
print(bool(a))

a = 0
print(bool(a))

a = -1
print(bool(a))

a = ""
print(bool(a))

print(1, 20, 30, 450, 100, 30123, 123123, 123123134, sep="#")  # 1#20#30#450#100#30123#123123#123123134
# print(1, 10, 30, end="\n"  # 1 10 30   表示末尾换行

x = "abfutyu"
y = "bbd"

print(x < y)  # True  如第一个字母可以达成比较关系,后面的就不进行比较

a = float(input("请输入您的考试成绩"))
print(80 <= a <= 100)
