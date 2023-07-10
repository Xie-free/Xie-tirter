# 列表推导式  字典推导式  集合推导式
# 旧的列表  -----> 新的列表

# 1. 列表推导式:   格式: [表达式 for 变量 in 旧列表]  或者 [表达式 for 变量 in 旧列表 if 条件]

# 过滤掉长度小于或者等于3的人名
name = ["tom", "lily", "xie", "jave", "html", "abc", "joker", "he"]
result = [i for i in name if len(i) > 3]
print(result)

result = [i.capitalize() for i in name if len(i) > 3]
print(result)

# 将 1-100之间能被3整除,组成一个新的列表
result = [i for i in range(100) if i % 3 == 0]
print(result)

# 0-5 偶数 0-10奇数
# [(偶数, 奇数), (), (), ()]    [(0, 1), (0, 3), (0, 5)]
new_list = [(x, y) for x in range(6) if x % 2 == 0 for y in range(11) if y % 2 != 0]
print(new_list)

# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]] ------> [3, 6, 9, 5]
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
new_list1 = [i[-1] for i in list1]
print(new_list1)

dict1 = {"name": "xie", "salary": 5000}
dict2 = {"name": "Yu", "salary": 50}
dict3 = {"name": "live", "salary": 6700}
dict4 = {"name": "like", "salary": 1990}

list1 = [dict1, dict2, dict3, dict4]

# if 薪资大于5000加200, 低于5000加500
result = [x["salary"] + 200 if x.get("salary") > 5000 else x["salary"] + 500 for x in list1 ]
print(result)

"""
def func(name):
    result = []
    for i in name:
        if len(i) > 3:
        i = i.capitalize()
        result.append(name)
    return result
    
def func():
    new_list = []
    for i in range(5):  # 外层做偶数
        if i % 2==0
            for j in range(10):
                if j%2 != 0
                new_list.append(i, j)
    return new_list
"""
