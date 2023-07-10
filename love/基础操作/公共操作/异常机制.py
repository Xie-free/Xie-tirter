# 语法错误和异常
# 语法错误:
# while True
#     print("------>")


# number = 100
#
#
# def func():
#     # global number
#     number += 1


# 异常:
# def chu(a, b):
#     return a / b
#
#
# # x = chu(1, 0)  # ZeroDivisionError: division by zero
# x = chu(3, 2)
# print("-------", x)

# 异常处理:
"""
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
[finally:
    无论是否存在异常都会被执行的代码]

情况1:
    try:
        有可能会产生多种异常
    except 异常的类型1:
        print()
    except 异常类型2:
        pass


    
"""


def func():
    try:
        num_1 = int(input("输入第一个数字:"))
        num_2 = int(input("输入第二个数字:"))
        num_oper = input("输运算符(+ - * / ):")
        if num_oper == "+":
            # + 加法
            num_sum = num_1 + num_2
            print("和是:", num_sum)
        elif num_oper == "-":
            # - 减法
            num_sum = num_1 - num_2
            print("差是:", num_sum)
        elif num_oper == "*":
            # * 乘法
            num_sum = num_1 * num_2
            print("积是:", num_sum)
        elif num_oper == "/":
            # / 除法
            num_sum = num_1 / num_2
            print("商是:", num_sum)
        else:
            print("符号出现错误")
    except ZeroDivisionError:
        print("除数不能为0")
    except ValueError:
        print("必须是数字")
    except FileNotFoundError:
        pass
    except NameError:
        pass
    except Exception:
        pass

func()

print("--------")
