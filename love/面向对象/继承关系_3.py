"""
编写一个简单的工资管理程序, 系统可以管理以下四类人:
工人(worker)  销售员(salesman)  经理(manager)  销售经理(salamander)
 所有的员工都具有员工号, 姓名, 工资等属性, 有设置姓名, 获取姓名, 获取员工号, 计算工资等方法.
1) 工人: 工人具有工作小时和时薪的属性, 工资计算法方法: 工作小时 * 时薪
2) 销售员: 具有销售额和提成比例的属性, 工资计算方法: 销售额 * 提成比例
3) 经理: 具有固定月薪的属性, 工资计算方法: 固定月薪
4) 销售经理: 工资计算方法: 销售额 * 提成比例 + 固定月薪
请根据以上要求设计合理的类, 完成以下功能:
    1) 添加所有类型的人员
    2) 计算月薪
    3) 显示所有人工资情况

"""


class Person:
    def __init__(self, num, name, salary):
        self.num = num
        self.n = name
        self.s = salary

    def __str__(self):
        return f"工号是{self.num}, 姓名{self.n}, 本月工资{self.s}"

    def get_Salary(self):
        return self.s


class Worker(Person):
    def __init__(self, num, name, salary, hours, per_hour):
        super().__init__(num, name, salary)
        self.h = hours
        self.p = per_hour

    def get_Salary(self):
        money = self.h * self.p
        self.s += money
        return self.s


class Salesman(Person):
    def __init__(self, num, name, salary, sale_money, percent):
        super(Salesman, self).__init__(num, name, salary)
        self.s_m = sale_money
        self.p_c = percent

    def get_Salary(self):
        money = self.s_m * self.p_c
        self.s += money
        return self.s


# 创建对象
w = Worker("001", "king", 2000, 160, 50)
s = w.get_Salary()
print("月薪是:", s)
print(w)
print("---------------------")

two = Salesman("002", "king_2", 5000, 5000000, 0.003)
s = two.get_Salary()
print(s)
print(two)

