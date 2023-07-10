fn1 = lambda: 100
print(fn1())

# 一个参数
fn2 = lambda a: a
print(fn2("Hell World"))

# 默认参数/缺省参数
fn3 = lambda a, b, c= 100: a+b+c
print(fn3(20, 50))
print(fn3(20, 50, 70))

# 可变参数：*args
fn4 = lambda *args: args
print(fn4(10, 20, 30, "Hello World"))
print(fn4(10, 20, 30, "Hello World", 40))
print(fn4(10))  # 返回值为元组

# 可变参数： **kwargs
fn5 = lambda **kwargs: kwargs
print(fn5(name="Python", age=16))
print(fn5(name="Python", age=16, gender="男"))

