# lambda function

# g = lambda x: x+x+x
# print(g(5))

# lambda fuction with filter
# l1 = [2,6,5,7,8,9,12,11,13,15,14,15,16,18,17]
# new_list = list(filter(lambda x: (x%2 != 0),l1))
# print("odd number is\n",new_list)

# map fuction with filter
# l1 = [2,6,5,7,8,9,12,11,13,15,14,15,16,18,17]
# new_list = list(map(lambda x: (x*2),l1))
# print("odd number is\n",new_list)

# from functools import reduce
# l1 = [ 5,8,12,14,16,18,23,100]
# sun = reduce((lambda x,y: x+y), l1)
# print(sun)

class Employee:
    def __init__(self,name,age,salary,gender):
        self.name =name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_details(self):
        print("The name of Employee is", self.name)
        print("The age of Employee is", self.age)
        print("The salary of Employee is", self.salary)
        print("The gender of Employee is", self.gender)

e1 = Employee("Rohan",25,250000,"Female")
e1.show_details()
