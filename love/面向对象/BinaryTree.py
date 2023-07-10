# 二叉树是每个节点最多有两个字数(分别称为左子树和右子树)的树结构
# 二叉树的第i层最多有2的(i-1)次方,常用于排序或查找
# 设计二叉树类,模拟二叉树创建、插入子节点以及前序遍历、中序遍历、和后序遍历等遍历方式
# 同时还支持二叉树中任意子树的节点遍历
class BinaryTree:
    def __init__(self, value):
        self.__left = None
        self.__right = None
        self.__data = value

    def insertLeftChild(self, value):  # 创建左子树
        if self.__left:
            print("__left child tree already exists.")
        else:
            self.__left = BinaryTree(value)
            return self.__left

    def insertRightChild(self, value):  # 创建右子树
        if self.__right:
            print("Right child tree already exists.")
        else:
            self.__right = BinaryTree(value)
            return self.__right

    def show(self):
        print(self.__data)

    def preOrder(self):  # 前序遍历
        print(self.__data)
        if self.__left:
            self.__left.preOrder()  # 遍历左子树
        if self.__right:
            self.__right.preOrder()  # 遍历右子树
        print(self.__data)

    def postOrder(self):  # 后序遍历
        if self.__left:
            self.__left.postOrder()
        if self.__right:
            self.__right.postOrder()
        print(self.__data)


if __name__ == "__main__":
    print("Please use me as a module.")
