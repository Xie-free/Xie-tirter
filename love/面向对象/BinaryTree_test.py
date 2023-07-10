import BinaryTree

root = BinaryTree.BinaryTree("root")
b = root.insertRightChild("B")
a = root.insertLeftChild("A")
c = a.insertLeftChild("C")
d = c.insertLeftChild("D")
e = b.insertRightChild("E")
f = e.insertRightChild("F")
root.postOrder()
print("-------------")
root.preOrder()