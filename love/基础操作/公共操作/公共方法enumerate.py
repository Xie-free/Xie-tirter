# enumerate(可遍历对象, start=0(可以不写默认为0))
list1 = ["jie", "xie", "rong"]
for i in enumerate(list1, ):
    print(i)
for i in enumerate(list1, start=-1):
    print(i)