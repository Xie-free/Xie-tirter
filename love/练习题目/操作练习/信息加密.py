"""
给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。
这里将字母表的z和a相连，如果超过了z就回到了a。
例如a="cagy", b=3,
则输出 ：fdjb

"""
a = "cagy"
alphabet = "abcdefghijklmnopqrstuvwxyz"
b = 3
for i in a:
    c = alphabet.find(i)
    if c + b > 26:
        c = c + b - 26
        a = a.replace(i, alphabet[c])
    elif c == 26:
        c = b
        a = a.replace(i, alphabet[c + b])
    elif c + b <= 26:
        a = a.replace(i, alphabet[c + b])

print(a)
