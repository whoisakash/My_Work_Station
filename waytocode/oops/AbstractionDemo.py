# class Employee:
#     __totalEmp = 0
#
#     def __init__(self):
#         Employee.__totalEmp = Employee.__totalEmp + 1
#
#     def showData(self):
#         print(Employee.__totalEmp)
#
#
# emp = Employee()
# emp.showData()


class Employee:

    __bonus = 1000

    def __init__(self):
        self.name = "Akash"
        self.salary = 10000



    def showData(self):

        def totalSalary(self):
            totalSalary = self.salary + Employee.__bonus
            print("Your salary after adding bonus : ", totalSalary)

        print(self.name)
        totalSalary(self)



emp = Employee()
emp.showData()


