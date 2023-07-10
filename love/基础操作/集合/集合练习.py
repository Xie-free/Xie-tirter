import random

code = set()
flag = True
s = "qweroqpweu1239187098xhzcvzbvbcvbsdfgsd"

while flag:
    code_list = ""
    for i in range(4):
        second = random.choice(s)
        code_list += second
    code.add(code_list)
    if len(code) == 5:
        flag = False

print(code)
