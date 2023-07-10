# 加密算法: md5  sha1  sha256
# base64
import hashlib

msg = "like_xie"
md5 = hashlib.md5(msg.encode("utf-8"))

print(md5.hexdigest())  # afe7c9fcea1f22f3630d152272d20f71  # 32

sha1 = hashlib.sha1(msg.encode("utf-8"))
print(sha1.hexdigest())  # 900a3b6160484549dba8ba70e30a0b6f7bc7f2cc  # 40

sha256 = hashlib.sha256(msg.encode("utf-8"))
print(sha256.hexdigest())  # e966d0f16bdee3b6736f122254416e9c3305ade3f5aebf6e38b5fcc0f2a437f1  # 64

password = "123456"

list1 = []

sha256 = hashlib.sha256(password.encode("utf-8"))
list1.append(sha256.hexdigest())

pwd = input("输入密码")
pwd = hashlib.sha256(pwd.encode("utf-8"))
pwd = sha256.hexdigest()
for i in list1:
    if i == pwd:
        print("登录成功")
