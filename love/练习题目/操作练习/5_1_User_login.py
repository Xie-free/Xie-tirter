"""
用户名或者手机号码登录+密码
用户名:全部小写,首字母不能是数字,长度必须6位以上
手机号码:纯数字  长度11
密码必须是6位数字

以上符合条件则进入下层验证:
判读用户名+密码   是否正确
"""
choice = input("请输入您选择的登录方式(用户名注册或者手机号注册)")
while True:
    if choice == "用户名":
        user_name = input("请输入您的用户名(小写,首字母不能是数字,长度六位以上):")
        if len(user_name) > 6 and user_name.islower() and user_name[0].isalpha():
            print("用户名可使用")
            user_password = input("请输入密码(必须是六位数字)")
            if len(user_password) == 6 and user_password.isdigit():
                print("密码格式正确,可使用")
                break
            else:
                print("密码格式错误")
        else:
            print("用户格式错误")
    elif choice == "手机号":
        phone_number = input("请输入您的手机号(纯数字,11位):")
        if len(phone_number) == 11 and phone_number.isdigit():
            print("手机号可使用")
            user_password = input("请输入密码(必须是六位数字)")
            if len(user_password) == 6 and user_password.isdigit():
                print("密码格式正确,可使用")
            else:
                print("密码格式错误")
                break
        else:
            print("手机号格式错误")
