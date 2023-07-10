students = {1: (11, 22), 2: (33, 44), 3: {55, 66}}


def number_num(num):
    if isinstance(num, dict):
        for name, age in num.values():
            print(f"名字{name}, 年龄{age}")


result = number_num(students)
print(result)
