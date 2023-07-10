# 每科学分总览
python_credits = 3
math_credits = 4
english_credits = 4
sport_credits = 2
military_credits = 2
philosophy_credits = 2
# 所有学分相加
sum_credits = python_credits + math_credits + english_credits + sport_credits + military_credits + philosophy_credits
# 用户输入每学分的金额
money = eval(input("请输入每学分学费金额:"))
# 用户输入每月的生活费
living_expenses = eval(input("请输入每个月的生活费:"))
# 每个学期的生活费按五个月计算
sum_living_expenses = living_expenses * 5
# 贷款金额不能超过学费和生活费总额的60%
loan = ((sum_credits * money) + sum_living_expenses) * 0.6
# 打印选修学分
print(f"你本学期选修了{sum_credits}个学分")
# 打印学费:为学分 * 每学分金额
print(f"你应缴纳的学费为{sum_credits * money}元")
# 打印贷款金额
print(f"本学期你能够贷款{loan:.2f}元")

