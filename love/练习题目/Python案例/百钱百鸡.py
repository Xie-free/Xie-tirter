# 公鸡最多买20只
for x in range(0, 20):
    # 母鸡最多买33只
    for y in range(0, 33):
        # 鸡崽的数量为100 - x - y
        z = 100 - x - y
        # 判断是否成立
        if 5 * x + 3 * y + z / 3 == 100:
            if x != 0 and y != 0 and z != 0:
                print(f"公鸡有{x}只, 母鸡有{y}只, 鸡崽有{z}只")
