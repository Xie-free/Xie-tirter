# 1. 准备数据
import random
teachers = ["a", "b", "c", "d", "e", "f", "g", "h"]
offices = [[], [], []]

# 2. 分配老师到办公室 ---- 取到每个老师放到办公室列表 --- 遍历老师列表数据
for name in teachers:
    # 列表追加数据 --- append（选中） extend insert
    num = random.randint(0, 2)
    offices[num].append(name)
print(offices)

# 为了贴合生活,把各个办公室子列表加一个办公室编号1. 2. 3
i = 1
# 3.验证是否分配成功
for office in offices:
    # 打印办公室人数
    print(f"办公室{i}的人数是{len(office)}, 老师的名字:")
    # 打印老师的名字
    for name in office:
        print(name)
    i += 1
