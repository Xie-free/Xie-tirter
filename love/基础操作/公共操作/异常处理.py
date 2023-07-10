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
    except Exception:
        pass

    如果是多个except, 异常类型的顺序需要注意, 最大的Exception 要放到最后

情况2: 获取Exception的错误原因
    try:
        有可能会产生多种异常
    except 异常的类型1:
        print()
    except 异常类型2:
        pass
    except Exception as err:
        print(err)  -------> err的内容就是错误原因:

    pop from empty list -----> 从空的列表中删除内容

"""


def func():
    try:
        num_1 = int(input("输入第一个数字:"))
        num_2 = int(input("输入第二个数字:"))
        num_oper = input("输运算符(+ - * / ):")
        if num_oper == "+":
            # + 加法
            num_sum = num_1 + num_2
        elif num_oper == "-":
            # - 减法
            num_sum = num_1 - num_2
        elif num_oper == "*":
            # * 乘法
            num_sum = num_1 * num_2
        elif num_oper == "/":
            # / 除法
            num_sum = num_1 / num_2
        else:
            print("符号出现错误")

        print("结果是:", num_sum)
        # 操作列表
        list1 = []
        list1.pop()  #
        # 文件操作
        # with open(r"F:\Python\python_word\b.TxT", "w") as w_stream:
        #     w_stream.write(f"本次运算结果是{num_sum}")
        with open(r"F:\Python\python_word\b.TxT", "r") as w_stream:
            print(w_stream.read())
    except ZeroDivisionError:
        print("除数不能为0")
    except ValueError:
        print("必须是数字")
    except Exception as err:
        print("出错了", err)


func()
