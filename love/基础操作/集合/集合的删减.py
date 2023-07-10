# remove()：删除集合中的指定数据,如果数据不存在则报错
s1 = {10, 20}
s1.remove(10)
print(s1)

# s1.remove(10)
# print(s1) 报错

s1.update([5, 50, 500, 19, 1])
# discard():删除集合中的指定数据,数据不存在也不会报错
s1.discard(50)
print(s1)
s1.discard(100)
print(s1)

# pop():数据删除某个数据,并返回这个数据
s2 = s1.pop()
print(s2)
print(s1)

