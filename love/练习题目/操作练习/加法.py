"""
1. 准备做加法运输的数据1 - 100 增量为1
2。 准备变量保存将来运算的结果
3. 循环做加法运算
4. 打印结果
5. 验证结果正确性
"""
i = 0
result = 0
c = 100
while i <= c:
    # 加法运算 前来个数的结果 + 第三个数 --每计算一次加法就更新一次result变量的值
    result += i
    i += 1
print(f"1加到{c}的计算结果{result}")
