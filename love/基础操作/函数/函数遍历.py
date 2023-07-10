book = [1, 2, 3, 4, 8, 9]
number = [1, 109, 50, 60, 40, 78]


def add_book(book_name):
    book.append(book_name)
    print("添加成功")


def show_book(books):
    for book_i in books:
        print(book_i)


add_book(10)
show_book(book)


# 大于50的数取出
def get_number(num):
    # new_number = []
    # for i in num:
    #     if i > 50:
    #         new_number.append(i)
    # print(new_number)
    new_number = [i for i in number if i > 50]
    print(new_number)


get_number(number)


# 小于50的数删除

def del_number(num_small):
    n = 0
    while n < len(number):
        if num_small[n] < 50:
            num_small.remove(num_small[n])
        else:
            n += 1
    print(num_small)


del_number(number)