"""
字典练习1
"""
a = False
while a:
    book = {"书名": "三体", "价格": 54, "作者": "刘慈欣", "出版社": "***出版社"}
    book["价格"] *= 0.8
    print(book)
    break

"""
字典练习二
books = [{},{}]
"""
b = False
while b:
    books = [
        {"书名": "《流浪地球》", "价格": 53, "作者": "刘慈欣", "出版社": "***出版社"},
        {"书名": "《三体》", "价格": 54, "作者": "刘慈欣", "出版社": "***出版社"}
    ]

    for i in books:
        i.pop("出版社")
        print(books)
    break


















