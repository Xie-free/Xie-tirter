import heapq  # 导入heapq模块
import random  # 导入随机数模块

data = random.sample(range(1000), 10)  # 生成随机数测试数据
# print(data)
heapq.heapify(data)  # 堆化随机测试数据
# print(data)
heapq.heappush(data, 30)  # 新元素入堆, 自动调整堆结构
# print(data)
heapq.heappush(data, 5)
print(data)
heapq.heappop(data)  # 返回并删除最小元素, 自动调整堆
# print(data)
heapq.heappop(data)
# print(data)
heapq.heappushpop(data, 1000)  # 弹出最小元素, 同时新元素入堆
# print(data)
heapq.heappushpop(data, 500)  # 弹出最小元素, 同时新元素入堆
heapq.heappushpop(data, 700)
print(data)
print(heapq.nlargest(3, data))  # 返回最多的前三个元素

print(heapq.nsmallest(2, data, key=str))  # 返回指定排序规则下最小的3个元素

