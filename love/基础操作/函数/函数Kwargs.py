"""
可变参数: **kwargs
关键字参数
在函数调用的时候必须传递关键字参数,才可以将其转换成key:value
装到字典

"""


# key word
def show_book(**kwargs):
    print(kwargs)  # {}
    for k, v in kwargs.items():
        print(k, v)


show_book(book_name="西游记", author="吴承恩", nuumber=5)
show_book(book_name="西游记")

print("-" * 100)

book = {'book_name': "西游记", 'author': "吴承恩", 'number': 5}
show_book(**book)   # --->