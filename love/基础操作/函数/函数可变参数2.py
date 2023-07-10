"""
可变参数:
*args  **kwargs
arguments

"""


def show_book(*args, **kwargs):
    print(args)  # ()
    print(kwargs)  # {}


book = {'book_name': "西游记", 'author': "吴承恩", 'number': 5}
show_book("666", 111)
show_book("谢", **book)

print(book, "hell", sep="--")  # 覆盖分隔符
print(book, "hell", "--")

print("{}{}{}".format("aa", "bb", "cc", "dd"))
print("{name}{age}{sex}".format(name="zhangsan", age=16, sex="男"))

result = "".join(["aa", "cc", "bb"])
print(result)