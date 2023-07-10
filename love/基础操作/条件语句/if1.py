import random

ran = random.randint(1, 100)
# print(ran)

guess = int(input("请输入您猜的数:"))
guess1 = guess

# if guess < ran:
#     print("您猜的数值小了")
# elif guess > ran:
#     print("您猜的数值大了")
# elif guess == ran:
#     print("您猜对了")
while guess != ran:
    if guess < ran:
        print("您输入的值小了")
        guess = int(input("请再次输入您猜的数值:"))
    elif guess > ran:
        print("您输入的值大了")
        guess = int(input("请再次输入您猜的数值:"))
print("您猜对了")