list1 = [1, 4, 2]
list2 = [1, 4, 2]
set1 = {i ** 2 for i in list1}
print(set1)
for i in list2:
    i ** 2
    list2.append(i)
print(list2)