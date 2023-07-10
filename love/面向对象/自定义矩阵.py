# 2.1模拟矩阵运算, 支持矩阵转置, 修改矩阵大小, 矩阵与数组的加、减、乘运算
# 以及矩阵与矩阵的加、减、乘运算.
class SimNumpyArray(object):
    def __init__(self, p):  # 构造函数
        """可以接受列表、元组、range对象等类型的数据,并且每个元素必须为数字"""
        if type(p) not in (list, tuple, range):
            print("data type error")
            return
        for item in p:
            # 下面这行用来判断参数类型
            if type(item) not in (int, float, complex):
                print("data type error")
                return
        self.__data = [list[p]]
        self.__row = 1
        self.__col = len(p)

    # 析构函数
    def __del__(self):
        del self.__data

    # 修改大小,首先检查给定的大小参数是否合适
    def reshape(self, size):
        # 参数必须为元组或列表, 如(row, col) 或 [row, col]
        # row 或col 其中一个可以为-1, 表示为自动计算
        if not (isinstance(size, list) or isinstance(size, tuple)):
            print("size parameter error")
            return
        if len(size) != 2:
            print("size parameter error")
            return
        if not isinstance(size[0], int) or (not isinstance(size[1], int)):
            print("size parameter error")
            return
        # 行数或列数为-1表示该值自动计算
        if size[0] == -1:
            if size[1] == -1 or (self.__row * self.__col) % size[1] != 0:
                pass