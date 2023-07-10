class Article:
    def __init__(self, name, author):
        self.n = name
        self.a = author

    def show(self):
        print(f"发表文章名字{self.n}, 作者:{self.a}")


class Tag:
    def __init__(self, name):
        self.n = name
