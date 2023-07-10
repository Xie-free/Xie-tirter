# 删除列表重复
# 方法一
a = [1, 2, 3, 4, 5, 1, 1, 3, 4, 1, 1, 1, 1]

for i in a[::-1]:
    if i == 1:
        a.remove(i)

print(a)

# 方法二
b = [1, 2, 3, 4, 5, 1, 1, 3, 4, 1, 1, 1, 1]

while 1 in b:
    b.remove(1)

print(b)

# 方法三
c = [1, 2, 3, 4, 5, 1, 1, 3, 4, 1, 1, 1, 1]
d = 0
c.insert(0, str(d))
for i in c:
    if i == 1:
        c.remove(i)
        c.insert(0, str(d))
        d += 1
for item in range(d + 1):
    del c[0]
print(c)

# 方法四
e = [1, 2, 3, 4, 5, 1, 1, 3, 4, 1, 1, 1, 1]

for i in range(e.count(1)):
    e.remove(1)

print(e)
