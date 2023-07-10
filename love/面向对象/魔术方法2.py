import sys

"""
__del__:
    1. 对象赋值
        p = Person
        p1 = p
        说明: p和p1共同指向同一个地址
        
    2. 删除地址的引用
        del p1  删除p1对地址的引用
    3. 查看对地址的引用次数:
        import sys
        sys.getrefcount(p)
    4. 当一块空间没有了任何引用， 就会默认执行__del__
        ref = 0

"""


# __del__: delete的缩写 析构魔术方法
# 触发时机: 当对象没有用(任何变量引用) 的时候触发
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("-----> del")


p = Person("jacker")
p1 = p
print(p1.name)
p2 = p
print(p2.name)

p1.name = "Tom"
print(p.name)
print(p2.name)

del p
print("删除p后打印", p2.name)
del p1
print("删除p1后打印", p2.name)
# del p
# print("删除p后打印", p.name)


print(sys.getrefcount(p2))
# 对象赋值
n = 5
n1 = n
