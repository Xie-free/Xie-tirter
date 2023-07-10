i = 1
result = 0
c = 2
g = 100
# 这里的g是从i到g的c次累计相加
while i <= g:
    if i % c == 0:
        result += i
    i += 1
print(f"1--{g}的{c}的结果为{result}")
