# 1.1自定义一个数组类,支持数组与数字之间的四则运算,数组之前的加法运算
# 内积运算和大小比较,数组元素访问和修改,以及成员测试等功能


class MyArray:
    def __init__(self, *args):
        if not args:  # 判断是否有元素
            self.__value = []  # 没有元素就设置一个空列表
        else:
            for arg in args:  # 有元素就遍历获得
                if not self.__isnumber(arg):  # 每次获得都要判断是否为数值类型
                    print("All elements must be numbers")  # 如果不是数值类型就打印
                    return
            self.__value = list(args)

    # 重载运算符+
    # 数组中每个元素都与数字n相加,或两个数组相加,返回新数组
    def __add__(self, n):
        if self.__isnumber(n):  # 判断要加的参数是否为数值
            # 数组中所有元素都与数字n相加
            b = MyArray()
            b.__value = [item + n for item in self.__value]
            return b.__value

        elif isinstance(n, MyArray):
            # 两个等长的数组对应元素相加
            if len(n.__value) == len(self.__value):
                c = MyArray()
                c.__value = [i + j for i, j in zip(n.__value, self.__value)]
                # zip函数将两个等长的列表压缩在一起,然后同时传给i和j
                # 并使两个相加之后然后再添加到空列表
            else:
                print("Length not equal")
        else:
            print("No supported")

    # 重载运算符-
    # 数组中每个元素都与数字n相减, 返回新数组
    def __sun__(self, n):
        if not self.__isnumber(n):  # 判断要加的参数是否为数值
            print("- operating with", type(n), "and number type is not supported")
            return
        else:
            if isinstance(n, MyArray):
                # 两个等长的数组对应元素相减
                if len(n.__value) == len(self.__value):
                    c = MyArray()
                    c.__value = [i - j for i, j in zip(n.__value, self.__value)]
                    # zip函数将两个等长的列表压缩在一起,然后同时传给i和j
                    # 并使两个相加之后然后再添加到空列表
                else:
                    print("Length not equal")

    @staticmethod
    def __isnumber(n):
        return isinstance(n, (int, float, complex))


x = MyArray(1, 2, 3, 4, 5, 6)
y = MyArray(1, 2, 3, 4, 5, 6)
x = x + 6
y = y + 10
print(x)
print(y)
