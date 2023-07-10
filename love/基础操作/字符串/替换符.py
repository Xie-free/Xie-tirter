ago = 18
name = "long"
weight = 55.5
stu_id = 5
print("今年我的年龄是%d岁" % ago)
print("我的名字是%s" % name)
print("我的体重是%.2f公斤" % weight)
print("我的学号是%03d" % stu_id)
print("我的名字是%s,今年%d岁了" % (name, ago))
print("我的名字是%s,明年%d岁了" % (name, ago+1))
print("我的名字是%s,今年%d岁了,我的体重是%0.2f公斤,我的学号是%03d" % (name, ago, weight, stu_id))
print(f"我的名字是{name}我的年龄是{ago}明年我的年龄是{ago+1}")

