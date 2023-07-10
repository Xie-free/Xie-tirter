from scipy import special as S

print(S.cbrt(8))  # 立方根
print(S.exp10(3))  # 10 ** 3
print(S.sindg(90))   # 正弦函数, 参数为角度
print(S.round(3.1))  # 四舍五入函数
print(S.round(3.5))
print(S.round(3.499))
print(S.comb(5, 3))  # 从5个中任选3个的组合数
print(S.perm(5, 3))  # 排列数
print(S.gamma(4))  # gamma函数
print(S.beta(10, 200))  # beta函数
print(S.sinc(0))  # sinc函数
print(S.sinc(1))