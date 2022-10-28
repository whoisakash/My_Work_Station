print("Login for Use Calculator")
user_name = str(input("Enter User Name:-"))
pass_word = str(input("Enter Password:-"))
print("login Successfully.\n Signup")
while True:
    signup_user_name = str(input("User Name:-"))
    signup_pass_word = str(input("Password :-"))

    def calculator():
        '''make claculator, by use loop   '''
        print("\nCalculate")
        num1 = int(input("enter number:- "))
        oper = str(input("Enter operation sign:- "))
        num2 = int(input("enter other number:- "))
        while True:
            if oper == "+":
                print(num1 + num2)
                calculator()
                # break
            elif oper == "-":
                print(num1 - num2)
                calculator()
                # break
            elif oper == "*":
                print(num1 * num2)
                calculator()
                # break
            elif oper == "/":
                print(num1 // num2)
                calculator()
                # break
            else:
                print("not valid input")
                calculator()
                # break
            break
    def check_id():
        if (signup_pass_word == pass_word) and (signup_user_name == user_name):
            calculator()

        else:
            print("\nInvalid Username or Password\n Sign up again")
    check_id()

# num = 786
# sum = 0
# while True:
#     if(num == 0):
#         break
#     else:
#         dig = num % 10
#         sum = sum+dig
#         num = num//10
# print("sum of ",786,"=",sum)

