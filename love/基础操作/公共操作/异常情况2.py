# 抛出异常 raise

# 注册 用户名必须6位
def register():
    user_name = input("输入用户名:")
    if len(user_name) < 6:
        raise Exception("用户长度必须6位以上")
    else:
        print("输入的用户名是:", user_name)


try:
    register()
except Exception as err:
    print(err)
    print("注册失败")
else:
    print("注册成功")
