"""
模拟论坛:

"""
msg = input("发表一句话")
print("*" * 50)
print("以下为回复内容:")
while True:
    # 输入用户名:
    user_name = input("用户名:")
    while True:
        # 输入回复内容:
        comment = input("请输入您的评论:")
        comment1 = comment.strip()
        # 验证内容
        if len(comment) != 0:
            # 验证长度是否超过20个字
            if len(comment) < 20:
                # 是否存在敏感词汇
                comment.replace("丑陋", "**")
                print(f"用户{user_name}发表的:\n{comment}")
                break
            else:
                print("评论内容不能大于20个字")
            # 成功则发出评论, 否则重新输入
    else:
        print("评论内容不能为空!")
