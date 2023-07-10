"""
二进制:0,1                          0x558 ----> 二进制
八进制:0,1,2,3,4,5,6,7              0b 0101   0101   1000
十进制:0~9                               5        5       8
十六进制:0~9 a~f
                                   0x826
十进制转二进制:                      0b 1000   0010   0110
10  ----> 二进制表示:                    8      2      6

函数:                              0xac3
bin()  # 0b                         0b   1010   1100   0011
int()                             0
oct()  # 0o
hex()  # 0x


已知二进制转成十六进制, 将二进制从右侧开始4为位一组,最后不足四位补0
已知二进制转八进制,将二进制从右侧开始三位一组,最后一组不足三位吧补0
"""


# 十进制转二进制  bin()
n = 149
result = bin(n)  # binary
print(result)  # 0b10010101

# 十进制转八进制  oct()
result = oct(n)
print(result)  # 0o225

# 十进制转十六进制  hex()
sixteen = 150
result = hex(sixteen)
print(result)  # 0x96

# 前缀: 0b  二进制   0o 八进制    0x 十六进制    默认十进制

hexadecimal = 0x558
print(int(hexadecimal))  # 1368
print(hexadecimal)  # 1368

decimal_system = 1368
print(hex(decimal_system))  # 0x558

print(bin(hexadecimal))  # 0b10101011000
# 向二进制转换, 无论当前参数是几进制

print(oct(hexadecimal))  # 0o2530
# 向八进制转换, 无论当前参数是几进制

