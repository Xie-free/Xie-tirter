# 需求：创造0-10的偶数列表
# 方法一：range()步长实现
list1 = [i for i in range(0, 10, 2)]
print(list1)

# 方法二：for循环加if 创造有规律的列表
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)

print(list2)

# 方法三：for循环配合if的代码 改写成带if的列标推导式
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)