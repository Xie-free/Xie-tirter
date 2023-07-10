# 产生两个随机整数1-10, 判断两个数字之间的和是否大于8并且差小于等于3,
# 如果是则显示:success，否则显示:fail
import random

a = random.randint(1, 10)
b = random.randint(1, 10)
print(a, b)
if (a + b) > 8 and abs(a - b) <= 3:
    print("success")

else:
    print("fail")

# 输入销售金额, 符合哪种奖励的范围
"""
1-5: 1000元
5-10： 奖励笔记本IBM
10-100: 奖励iphone12
超过了100: 奖励特斯拉
如都不达到
鼓励奖

"""
money = int(input("请输入您的销售金额"))
if 1000 < money <= 5000:
    print("奖励100元")
elif 5000 < money <= 10000:
    print("奖励笔记本IBM")
elif 10000 < money <= 100000:
    print("奖励iphone12")
elif money > 100000:
    print("奖励特斯拉")
else:
    print("鼓励奖")
