a = 3
b = 5
m = max(a, b)
mi = min(a, b)
for i in range(1, m+1):
    if (mi * i) % m == 0:
        print(mi * i)
        break
