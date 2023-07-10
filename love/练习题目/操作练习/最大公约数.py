def convention(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(small + 1):
        if a % (small - i) == 0 and b % (small - i) == 0:
            return small - i


print(convention(6, 9))
