# 局部变量
# 定义一个函数，声明一个变量：函数体内部访问一次,函数体外面访问一次
def tast():
    a = 100
    print(a)

tast()
a = 101
print(a)
# 全局变量
a = 100
def tast():
    print(a)


def tast1():
    print(a)

tast()

tast1()

# 修改全局变量
def tast():
    print(a)
# 总结：
# 1.如果在函数里面直接把函数的变量a = 200 赋值,此时修改的是局部变量,全局变量无变化
# 2.函数体内部修改全局变量：先global声明修改的变量为全局变量,然后再重新赋值

def tast1():
    global a # 声明为全局变量a
    a = 200
    print(a)
tast1()

print(f"全局变量a= {a}")
