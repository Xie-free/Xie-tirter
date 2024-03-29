# 缺省参数也叫默认参数,用于定义函数,为参数提供默认值,调用函数时可不传该默认参数的值
# (注意:所有位置参数必须出现在默认参数前,包括函数定义和调用).
def user_info(name, age, gender = "男"):
    print(f"您的名字时{name}, 年龄时{age}, 性别是{gender}")

user_info("Jie", 18)  # 没有为缺省参数传值,表示使用默认值
user_info("Jie", 16, "女")  #为缺省参数传值,使用这个值,即修改了默认参数
# 函数调用时, 如果为缺省参数传值则修改默认参数值, 否则使用这个默认值



