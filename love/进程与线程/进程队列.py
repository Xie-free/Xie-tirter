# 进程间通信
from multiprocessing import Queue

q = Queue(5)
q.put("A")
q.put("B")
q.put("C")
q.put("D")
q.put("E")
print(q.qsize())
if not q.full():  # q.full意思是队列是否为零  q.empty()  判断队列是否是空的
    q.put("F", timeout=3)  # put() 如果queue满了则只能等待, 除非有"空地"则添加成功
else:
    print("队列已满")
# q.put_nowait("G")
# q.get_nowait()

# 获取队列的值
def func(s=2):
    print(q.get(timeout=s))


func()
func()
func()
func()
func()
func()


