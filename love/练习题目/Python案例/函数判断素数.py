def prime_number(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return "False"
    else:
        return "True"


print(prime_number(int(input("请输入要判断的正整数"))))
