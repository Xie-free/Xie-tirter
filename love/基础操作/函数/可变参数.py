# 不定长参数也叫可变参数. 用于不确定调用的时候会传递多少个参数(不传参也可以)的场景.
# 此时,可以用包裹(packing)位置参数，或者包裹关键字参数,来进行参数传递,会显得非常方便
def user_info(*args):
    print(args)

user_info("Jie")

user_info("Jie", 18)

user_info("Jie", 18, "女")

user_info()
# 元组形式

# 包裹关键字传递
def user_info(**kwargs):
    print(kwargs)

user_info()
user_info(name="Jie", age=16)
user_info(name="Jie", age=18, gender= "女")

# 字典形式
# 无论时包裹位置传递还是包裹关键字传递,这都是一个组包的过程



