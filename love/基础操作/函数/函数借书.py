is_login = False


def login(user_name, user_password):
    if user_name == "xie" and user_password == "520":
        print("登录成功")
        global is_login
        is_login = True
    else:
        print("登录失败")


def borrow_book(book_name):
    if is_login:
        print(f"成功借阅{book_name}")
    else:
        print("用户没登录,无法借书")
        user_name = input("用户名:")
        user_password = input("密码:")
        login(user_name, user_password)


login("xie", 510)
borrow_book("dasfs")
borrow_book("daljkasd")
