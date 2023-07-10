"""
默认值参数: 在定义函数的时候,有一个或者多个参数已经赋好值.
def 函数名(参数1， 参数2， 参数3 = 值, 参数4 = 值， 参数5 = 值):
    pass

调用特点
函数名(参数1， 参数2)

注意:
1.在定义函数的时候，普通参数要位于默认值参数的前面
2.默认参数的顺序是固定的
关键字参数
borrow_book("aaa", '小明', school="北科")

"""


def borrow_book(book_name, user_name, number=1, school="1000phone"):
    print(f"进入{school}借书系统.......")
    print(f"{user_name}要借阅的书名是:{book_name},借阅的数量是{number}")


# borrow_book("aaa")
borrow_book("aaa", 6)
borrow_book("aaa", '小明', school="北科")
