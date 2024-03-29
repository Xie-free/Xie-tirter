"""
位运算:
&   |   ^   ~   <<   >>>
&  类似  and

F and F ---> F
T and T ---> T
"""
n1 = 0b0110  # 6
n2 = 0b0010  # 2

"""
1 为 真   0 为假
n1 = 0b0110  # 6
n2 = 0b0010  # 2
0&0 --->0
1&1 --->1
1&0 --->0
0&0 --->0
0b0010  ----> 十进制:2

5 & 9 ---->1
0101
1001

0b0001 --->1
"""

print(n1 & n2)
print(5 & 9)

print("*" * 20)
print(n1 | n2)  # 6
print(5 | 9)  # 13

print("*" * 20)
print(n1 ^ n2)  # 4
print(5 ^ 9)  # 12
"""
异或:  上下两个数位相同为0,不同则为1

n1 = 0b0110  # 6
n2 = 0b0010  # 2
---------------
        0100
0101
1001
----
1100 ---> 12

"""

print("*" * 20)
print(~n1)  # -7
print(~5)   # -6

"""
n1 = 0b0110
bit byte
1byte = 8bit
n = 2
1G ---> 1024m

二进制的负数表示:
原码  0110
反码  1001
补码  反码+1
  1001
+    1
------------
  1010

已知: 二进制:   1110 1010   十进制的表示?
  1111 1010    补码
-         1
-----------------
  1111 1001    ---->  反码
原码:    00000 0110 ----> 6
-6

明确:
1.已知十进制负数, 求二进制负数:
    1.正数的原码  2.原码取反  3. 加1
    -7的进制:
      步骤:
      1.先求+7的二进制: 00000 0111 原码
      2.反码: 1111 1000
      3.补码: 1111 1001
      -7的二进制是: 1111 1001
2.已知二进制的负数(判断是否是负的二进制的依据,看二进制的高位:1111 1010, 最高位是1则为负0则为正数), 求对应的十进制。
    1.二进制(负的)   2. 二进制减1    3.取反    4.原码 将原码转成十进制,在十进制的前面加负号
    已知:二进制: 1111 1010, 十进制的表示?
    1111 1010    补码
-         1
-----------------
  1111 1001    ---->  反码
原码:    00000 0110 ----> 6
-6    
      
         
"""
















