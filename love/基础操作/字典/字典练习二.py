"""
字典练习三
book = []  框  能放多本书
书:{}
书名  作者  价格

添加三本书

1.  添加书
    不能添加同名书籍
    [{"书名":"aaa",......},{"书名":"aaa"}]
"""
book = []

while True:
    if len(book) == 3:
        break

    name = input("请输入书籍名称")
    for i in book:
        if name == i.get("name"):
            print("书籍重复")
            break
    else:
        author = input("请输入书籍作者")
        price = input("请输入书籍价格")
        book.append({
            "name": name,
            "author": author,
            "price": price
        })

print(book)