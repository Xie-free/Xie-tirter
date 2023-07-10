"""
给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO
回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".
示例：
输入：a = "abcba"  n = 5
输出：YES

"""
a = "abcba"
n = 5
count = len(a)
inverted = a[::-1]
for i in a:
    b = a.find(i)
    if n <= count:
        result = a[b:n]
        if result in inverted:
            print("YES")
            break
    elif n > count:
        n -= count
        result = a[b:n]
        if result in inverted:
            print("YES")
            break
else:
    print("NO")