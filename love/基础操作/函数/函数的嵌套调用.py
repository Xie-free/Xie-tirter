# 两个函数 testA 和 testB  -- 在A里面嵌套调用B
# B函数
def testB():
    print("B函数开始-----")
    print("这是函数B-----")
    print("B函数结束-----")

# A函数
def testA():
    print("A函数开始-----")
    # 嵌套调用B
    testB()
    print("A函数结束-----")
testA()