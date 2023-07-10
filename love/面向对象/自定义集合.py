class Set(object):
    def __init__(self, data=None):
        if data is None:
            self.__data = []
        else:
            if not hasattr(data, "__iter__"):
                # 判断提供的数据是否为可迭代对象, 实例化失败
                raise Exception("必须提供可迭代的数据类型")
        temp = []
        for item in data:
            # 集合中的元素必须可哈希
            hash(item)
            if item not in temp:
                temp.append(item)
        self.__data = temp

    # 析构方法
    def __del__(self):
        del self.__data

    # 添加元素, 要求元素必须可哈希
    def add(self, value):
        hash(value)
        if value not in self.__data:
            self.__data.append(value)
        else:
            print("元素已存在, 操作被忽略")

    # 删除元素
    def remove(self, value):
        if value in self.__data:
            self.__data.remove(value)
            print("删除成功")
        else:
            print("元素不存在, 删除操作被忽略")

    # 随机弹出并返回一个元素
    def pop(self):
        if not self.__data:
            print("集合已空, 弹出操作被忽略")
        else:
            return self.__data.pop()

    def show(self):
        print(self.__data)


x = Set(range(10))  # 创建集合对象
y = Set(range(8, 15))
z = Set([1, 2, 3, 4, 5])
x.show()
y.show()
z.show()

z.add(6)  # 增加元素
z.show()
z.remove(3)  # 删除指定元素


