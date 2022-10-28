# class Company:
#     def showData(self, comName):
#         print(comName)
#
# com = Company()
# com.showData("Waytocode")


# class Employee:
#     def __init__(self):
#         self.empName = "Akash"
#
#     def showData(self):
#         print(self.empName)
#
# emp = Employee()
# emp.showData()

# Arguements
class Employee:
    def __init__(self, empName):
        self.empName = empName

    def showData(self):
        print(self.empName)

emp = Employee("Akash Coder")
emp.showData()


