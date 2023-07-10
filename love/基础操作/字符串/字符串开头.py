mystr = "hello world and itcast and itheima and Python"
# 1. startswith(字符串，开始下标，结束下标)：判读字符串是否以某个子串开头
# *开始下标和结尾下标可以不写，不写就是以整个字符串开始
# *startswith输入结果为布尔型True 或 False
print(mystr.startswith("hello"))

# 2. endswith(字符串，开始下标，结尾下标)：判读字符串是否以某个子串结尾
# *开始下标和结尾下标可以不写，不写就是以整个字符串开始
# *endswith输入结果为布尔型True 或 False
print(mystr.endswith("Python"))
