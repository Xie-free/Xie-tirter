x = 3
print("id(x):", id(x))
y = x
print("id(y):", id(y))

x += 3
print("id(x)加3之后的id:", id(x))
print("x:", x)
print("id(y)的id", id(y))
print("y:", y)
