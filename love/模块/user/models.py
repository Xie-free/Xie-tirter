__all__ = ["User"]  # 只是针对 from 包.模块 import *

version = "1.1"


class User:
    def __init__(self, user_name, user_password):
        self.u_n = user_name
        self.u_p = user_password

    def login(self, user_name, user_password):
        if user_name == self.u_n and user_password == self.u_p:
            print("登录成功")
        else:
            print("登录失败!")

    def show(self):
        print(self.u_n, self.u_p)

    def publish_article(self, article):
        print(f"{self.u_n}, 发表了文章:{article.n}")


if __name__ == "__main__":
    print("------------------user-------------")
