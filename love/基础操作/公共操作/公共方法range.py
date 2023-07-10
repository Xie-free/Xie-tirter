# range(start,end,step)
for i in range(1, 10, 1):
    print(i)  # 1 2 3 4 5 6 7 8 9
print(range(1, 10, 1))

j = 2
i = 1
for i in range(1, 100, 1):
    i %=j
    print(i)
    i+=1

