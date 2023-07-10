# 输入成绩
student_scores = eval(input("请输入学生成绩:"))
# 判断
if student_scores >= 90:
    print("A")
elif 80 <= student_scores < 90:
    print("B")
elif 70 <= student_scores < 80:
    print("C")
elif 60 <= student_scores < 70:
    print("D")
else:
    print("E")