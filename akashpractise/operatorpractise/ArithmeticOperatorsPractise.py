# arithmetic operator.
print("Arithmatic Operator Practise")
# print ("select code \n1 for + \n2 for - \n3 for * \n4 for /")
num1 = input("\nEnter 1st num:- ")
num2 = input("Enter 2nd num:- ")
# input_code = int(input("Enter Code from 1 to 4 :- "))
    # if input_code = :
    #     print(f"", {num1},"+", {num2},"=", {num1 + num2})
num_addition = int(num1) + int(num2)
print("Addition is", num_addition)

num_minus = int(num1) - int(num2)
print("Minus is", num_minus)

num_multiplication = int(num1) * int(num2)
print("Multiplication is", num_multiplication)

num_division = int(num1) / int(num2)
print("Division is", num_division)

num_exponential = int(num1) ** int(num2)
print("Exponential is", num_division)

num_floor = int(num1) // int(num2)
print("Floor division is", num_floor)

num_modulo= int(num1) % int(num2)
print("Modulo is", num_modulo)