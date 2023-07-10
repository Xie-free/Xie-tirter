# 位置参数：调用函数时根据函数定义的参数位置来传递参数
def user_info(name, ago, gender):
    print(f"您的名字是{name},年龄是{ago}， 性别是{gender}")

# 传递和定义参数的顺序及个数必须一致
# user_info("xie", 16, "女")
# user_info("xie", 16) # 个数定义和传入不一致会报错
# user_info(16, "xie", "女") # 顺序也和定义必须是一致的, 否则导则数据无意义
