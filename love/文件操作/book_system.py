# 持久化保存: 文件
# list 元组, 字典 ----> 内存

# 用户注册
def register():
    user_name = input("输入用户名:")
    password = input("输入密码:")
    re_password = input("输入确定密码:")
    if password == re_password:
        # 保存信息
        with open(r"F:\python\book\user.TXT", "a") as w_stream:
            w_stream.write(f"{user_name}   {password}\n")

        print("用户注册成功")
    else:
        print("密码不一致!")


def login():
    user_name = input("输入用户名:")
    password = input("输入密码:")
    if user_name and password:
        with open(r"F:\python\book\user.TXT", "r") as r_stream:
            while True:
                user = r_stream.readline()  # admin 123456
                if not user:
                    print("用户名或密码输入有误")
                    break
                input_user = f"{user_name}   {password}\n"
                if user == input_user:
                    print("用户登录成功")
                    break


def show_book():
    print("-------图书馆书架---------")
    with open(r"F:\Python\book\books.txt", "r") as r_stream:
        books = r_stream.readlines()
        for book in books:
            print(book)


# 调用函数
# register()
# login()
show_book()
