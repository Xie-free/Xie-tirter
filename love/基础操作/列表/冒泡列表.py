a = [5, 3, 4, 6, 7, 8, 2, 10, 18]

for j in range(0, len(a) - 1):
    for i in range(0, len(a) - 1 - j):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

print(a)