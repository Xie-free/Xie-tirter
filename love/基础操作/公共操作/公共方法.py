t1 = (1, 2, 10, 49, 565, 534, 23, 4)
t2 = [1, 2, 10, 49, 565, 534, 23, 4]

# 排序 sorted
result = sorted(t1)
result1 = sorted(t1, reverse=True)
print(result)
print(result1)

# 最大max 最小min
result2 = max(t2)
result3 = min(t2)
print(result2)
print(result3)

# 求和sum 绝对值abs
result4 = sum(t2)
result5 = abs(-5)
print(result4)
print(result5)

# chr  给ASSCII码值返回给值对应的字母
a = chr(68)
print(a)

# ord  给字母返回ASSCII码值
b = ord(a)
print(b)