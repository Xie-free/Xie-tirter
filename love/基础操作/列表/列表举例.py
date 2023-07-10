name_list = ["谢容容", "黑姬结灯"]
like_people = input("请输入喜欢的人：")

if like_people in name_list:
    print(f"您输入的名字是{like_people}, 此用户名在心上人中，心上人名单为{name_list}")
    print("恭喜您输入成功，猜对啦")
else:
    print(f"您输入的名字是{like_people}, 不对哦，看来你还是不够了解我")
print(type(like_people))