def print_hi_human():  # 无参无返回值的函数
    print("人类,你好")


def say_hi_human():  # 无参有返回值的函数
    return "人类,你好"


def say_hi_person(full_name):  # 有参有返回值的函数
    return f"{full_name},你好"


def say_hi_gender(full_name, gender):
    return f"尊敬的{full_name}先生/女士,欢迎来到火星"


def say_hi_default(full_name, gender="男"):
    return f"尊敬的{full_name}先生/女士,欢迎来到火星"


def say_hi_multi_parameter(*args):
    for i in args:
        print(f"{i}, 你好!")

