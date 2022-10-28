#
# print("Hello World")
#
# # Get name input and print Hello "name"
# your_name = input(str("Enter Your Name :- "))
# # print("Hello ",str(your_name))

# var1 = 52
# var2 = 14
# print(str(var1)+str(var2)) # string addition
# # print(int(var1+var2)) # integer addition

''' addition subtraction multiplication division'''
print("Seclect number for test MATH CALCULATION(+ - * /)")
select_first_number = input("\nSelect Your First Number:- ")
select_Second_number = input("Select Your Second Number:- ")

addition = int(select_first_number) + int(select_Second_number)
print(f"\nAddition of ", select_first_number, " &", select_Second_number," is ",addition)

subtraction = int(select_first_number) - int(select_Second_number)
print(f"\nSubtraction of ", select_first_number, " &", select_Second_number," is ",subtraction)

multiplication = int(select_first_number) * int(select_Second_number)
print(f"\nMultiplication of ", select_first_number, " &", select_Second_number," is ",multiplication)

division = int(select_first_number) / int(select_Second_number)
print(f"\nDivision of ", select_first_number, " &", select_Second_number," is ",division)