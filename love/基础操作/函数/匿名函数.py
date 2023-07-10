"""
匿名函数定义格式:

lambda 参数列表: 运算表达式

"""""


def test(a):
    return a + 1


print(test)
result = test(5)
print(result)

b = lambda a: a + 1
result = b(3)
print(result)

c = lambda x, y: x + y
result = c(1, 2)
print(result)
