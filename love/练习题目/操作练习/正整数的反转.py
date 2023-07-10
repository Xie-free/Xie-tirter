num = int(input("请输入您的需要反转的正整数"))
a = 0
while num > 0:
    a = a * 10 + num % 10
    num //= 10

print(a)
