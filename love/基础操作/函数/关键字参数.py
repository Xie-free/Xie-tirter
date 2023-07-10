# 函数调用, 通过”键=值“形式加以指定.可以让函数更加清晰,容易使用,同时也清除了参数的顺序需求.
def user_info(name, age, gender):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")

user_info("jie", age = 18, gender = "女")  # 您的名字是jie, 年龄是18, 性别是女
user_info("jie", gender = "女", age = 18)  # 您的名字是jie, 年龄是18, 性别是女

# 函数调用时,如果有位置参数时,位置参数必须在关键字参数的前面,但关键字参数之间不存在先后顺序

# 位置参数必须写在关键字参数的前面
# user_info(age = 18, gender= "女", 'jie')
