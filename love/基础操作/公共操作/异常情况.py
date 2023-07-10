# 异常情况
"""
# 文件操作   stream = open(....)  stream.read()   stream.close()
# 数据库操作  close()
try:
    pass
except:
    pass
finally:
    pass

"""


def func():
    r_stream = None
    try:
        r_stream = open(r"F:\Python\python_word\a.TXT", "r")
        container = r_stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print("-----finally")
        if r_stream:
            r_stream.close()
            print("------进入-----")
        return 3


x = func()
print(x)
