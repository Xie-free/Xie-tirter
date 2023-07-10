"""
1. 请写出一段python代码实现分组一个list里面的元素,比如[1,2,3,......100]变成[[1,2,3],[4,5,6],...]
2. 找出里面名字含有两个'e'的放到新列表中:
name = [['Tom', 'Billy', 'Jefferson','Andrew', 'Wesley', 'Steven', 'Joe']
        ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

"""

# 1.
list1 = [[x, x + 1, x + 2] for x in range(1, 100, 3)]
print(list1)

a = [i for i in range(1, 101)]
b = [a[y:y + 3] for y in range(0, len(a), 3)]
print(b)

# 2.
name = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
        ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

new_name = [j for i in name for j in i if j.count("e") >= 2]
print(new_name)
