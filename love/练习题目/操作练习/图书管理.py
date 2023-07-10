"""
图书管理系统
至少五本书
libray = [{},{}]
书名可以一样,但作者不可重复

1.借书
2.还书
3.查询(书名/作者)
4.查看所有
5.退出

"""
import time


libray = [
    {"书名": "红楼梦", "作者": "曹雪芹", "价格": 100, "number": 40},
    {"书名": "西游记", "作者": "吴承恩", "价格": 100, "number": 40},
    {"书名": "三国演义", "作者": "罗贯中", "价格": 100, "number": 40},
    {"书名": "水浒传", "作者": "施耐庵", "价格": 100, "number": 40}
]
libray_list = []

while True:
    choice = input("\n1.借书\n2.还书\n3.查询\n4.查看所有\n5.退出\n")
    if choice == "1":
        for book in libray:
            print(f"图书名:{book['书名']}, 作者:{book['作者']}, {book['价格']}, 库存:{book['number']}")
        check = input("请输入借阅的书籍名:")
        for i in libray:
            a = 0
            if check == i.get("书名"):
                a += 1
                if a == 1:
                    libray_list.append(i)
                    i["number"] -= 1
                    print("借阅成功")
                    break
                elif a > 1:
                    print(f"请问你要借阅哪一本{i}")
            else:
                print("找不到书籍")
    elif choice == "2":
        choice1 = input("请选择根据(书名/作者)还书")
        if choice1 == "书名":
            choice_name = input("请输入书名")
            for i in libray:
                if choice_name == i.get("书名"):
                    print(i)
                    continue
                else:
                    print("书名不存在")
    elif choice == "3":
        choice1 = input("请选择根据(书名/作者)查询")
        if choice1 == "书名":
            choice_name = input("请输入书名")
            for i in libray:
                if choice_name == i.get("书名"):
                    print(i)
                    continue
                else:
                    print("书名不存在")

        elif choice1 == "作者":
            choice_author = input("作者:")
            for i in libray:
                if choice_author == i.get("作者"):
                    print(i)
                    break
                else:
                    print("作者不存在")
        else:
            print("请选择规范输入")

    elif choice == "4":
        for book in libray:
            print(f"图书名:{book['书名']}, 作者:{book['作者']}, 价格:{book['价格']}, 库存:{book['number']}")
    elif choice == "5":
        print("正在为您退出")
        time.sleep(5)
        break

for book_1 in libray_list:
    print(f"图书名:{book_1['书名']}, 作者:{book_1['作者']}, 价格:{book_1['价格']}")
