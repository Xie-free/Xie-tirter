# student  book  computer

"""
知识点:
1. has a
    一个类中使用了另外一种自定义的类型

    student 使用computer  book
2. 类型:
    系统类型:
        str  int  float
        list  dict  tuple  set
    自定义类型:
        算是自定义的类, 都可以将其当成一种类型
        s = Student()
        s是Student 类型的对象

"""
class Computer:
    def __init__(self, brand, type, color):
        self.b = brand
        self.t = type
        self.c = color

    def online(self):
        print(f"正在使用{self.b}品牌电脑上网")

    def __str__(self):
        return f"品牌:{self.b}" \
               f"类型:{self.t}" \
               f"颜色:{self.c}"


class Book:
    def __init__(self, b_name, author, number):
        self.b_n = b_name
        self.a = author
        self.n = number

    def __str__(self):
        return f"书名:{self.b_n}" \
               f"作者:{self.a}" \
               f"数量:{self.n}"


class Student:  # has a
    def __init__(self, name, book, computer):
        self.n = name
        self.b = book
        self.c = computer
        self.books = []
        self.books.append(book)

    def borrow__book(self, book):
        for book1 in self.books:
            if book1.b_n == book.b_n:
                print(f"已经存在{book1.b_n}")
                break
            else:
                # 将参数book添加到列表中
                self.books.append(book)
                print("添加成功")

    def show_book(self):
        for book in self.books:  # book就是一个book对象
            print(book.b_n)

    def __str__(self):
        return f"{self.n}------------{self.c}------------{self.books}"


# 创建对象

computer = Computer("mac", "mac_pro2022", "深灰色")

book = Book("盗墓笔记", "南派三叔", 10)

stu = Student("xie_xie", book, computer)
print(stu)

# 看借了哪些书
stu.show_book()
book_1 = Book("鬼吹灯", "天下霸唱", 8)

stu.borrow__book(book_1)

print("----------------------")

stu.show_book()
