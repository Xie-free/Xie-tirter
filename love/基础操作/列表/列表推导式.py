# 作用:用一个表达式创建一个有规律的列表或控制一个有规律列表
# 列表推导式又名列生成式
# 列表推导式: 最终结果得到一个列表
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 列表推导式实现------
list3 = [i for i in range(10)]
print(list3)

# 0-100 之间得偶数  存放在列表中
# 方法一
list4 = [i for i in range(0, 101, 2)]
print(list4)

list5 = [i for i in range(0, 101) if i % 2 == 0]
print(list5)

# 取出a里面的单词
a = ["69", "hello", "20", "python", "100", "word", "high"]
list6 = [word for word in a if word.isalpha()]
print(list6)

# 取出a里面的单词,如果是h开头的则将首字母大写，不是h开头的全转大写
# 格式3：[结果1 if 条件 else 结果2 for 变量 in 可迭代的对象]
# 如果有(if else 结构) 结构要放在for 前面
list7 = [words.title() if words.startswith("h") else words.upper() for words in a if words.isalpha()]
print(list7)

new_list = []
for i in range(1, 10):
    for j in range(1, 10):
        new_list.append((i, j))
print(new_list)

list1 = [(i, j) for i in range(1, 10) for j in range(1, 10)]
print(list1)