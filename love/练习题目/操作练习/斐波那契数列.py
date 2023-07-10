a = 0
b = 1
list1 = []
list2 = []
for i in range(20):
    a, b = b, a + b
    list1.append(a)

print(list1)


# 函数
def num(c, d):
    for item in range(20):
        c, d = d, c + d
        list2.append(c)
    return list2


print(num(0, 1))
