list1 = [1, 2, 3, 4, 5, 6, 7]
"""
list --->  tuple, set("长度可能发生变化")
tuple ---> list, set
set  --->  list, tuple

dict ---> list, tuple, set  但只转化键,值不会转换
list ---> dict
"""
# 要求如下, 其他形式基本无法转化
list2 = [("a", 100), ("b", 10)]
list3 = [["a", 100], ["b", 10]]
list4 = [["a", [100, 1, 2]], ["b", 10]]
print(dict(list2))
print(dict(list3))
print(dict(list4))
