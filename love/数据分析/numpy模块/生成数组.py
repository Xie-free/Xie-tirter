import numpy as np

print(np.array([1, 2, 3, 4, 5]))  # [1 2 3 4 5]  # 把列表转换成数组
print(np.array((1, 2, 3, 4, 5)))  # 与上述相同, 把元组转换成数组
print(np.array(range(1, 6)))  # 与上述相同, 把range对象转换成数组
print(np.array([[1, 2, 3], [4, 5, 6]]))  # 二维数组
print(np.arange(8))  # 类似于内置函数range()
print(np.arange(1, 10, 2))  # 类似于内置函数range()
print(np.linspace(0, 10, 11))  # 生成一个等差数列,从零开始到十,生成十一个等差数列
print(np.linspace(0, 10, 11, endpoint=False))  # 不包含终点
print(np.logspace(0, 100, 10))  # 对数数组
print(np.logspace(1, 6, 5, base=2))  # 对数数组,相当于 2 ** np.linespace(1, 6, 5)
print(np.zeros(3))  # 全0一维数组
print(np.ones(3))  # 全1一维数组
print(np.zeros((3, 3)))  # 全0二维数组, 3行3列
print(np.zeros((3, 1)))  # 全0二维数组, 3行1列
print(np.zeros((1, 3)))  # 全0二维数组, 1行3列
print(np.ones((1, 3)))  # 全1二维数组
print(np.ones((3, 3)))  # 全1二位数组
print(np.identity(3))  # 单位矩阵
print(np.identity(2))
print(np.empty((3, 3)))  # 空数组, 只申请空间而不初始化, 元素值是不确定的