# 一种方法
# for a in range(1, 10):
#     for b in range(1, a+1):
#         print(f"{b} * {a} = {a * b}", end="\t")
#     print()

# 第二种
# for a in range(1, 10):
#     for b in range(a, 10):
#         print(f"{a} * {b} = {a * b}", end="\t")
#     print()

# 第三种
for i in range(1, 10):
    j = 1
    while j <= 9:
        print(f"{i} * {j} = {i * j}", end="\t")
        j += 1
    print()
