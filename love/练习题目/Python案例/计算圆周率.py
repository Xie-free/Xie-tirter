pi = 0
i = 1
j = 1
while 1 / i >= 1e-8 :
    pi = pi + j * 1 / i
    i = i + 2
    j = - j
else:
    print(f"{pi * 4}")
