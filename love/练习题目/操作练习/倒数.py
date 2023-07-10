def digitize(n):
    n = str(n)
    n = n[::-1]
    a = []
    for i in n:
        a.append(i)
    return a


b = digitize(123812)
print(b)
