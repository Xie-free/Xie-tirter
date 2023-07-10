# 等差数列
list1 = []
i = int(input("等差数列a1"))
e = i
m = int(input("等差数列的最后一项"))
d = int(input("等差数列的公差"))
b = 0

while i <= m:
    print(i)
    b = b + i
    i += d
    list1.append(i)
for item in range(len(list1)):

    if list1[item] == m:

        print("最后一位能根据第一位和公差求出来")
        break

if (m-i) % d != 0:
    print("最后一项无法根据公差和第一位求出来")


print(f"{e}到{m}和为{b},公差为{d}")


