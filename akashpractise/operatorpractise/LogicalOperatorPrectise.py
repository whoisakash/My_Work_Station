# Logical Operator = and, or, not

input_1 = input("Enter the input 1:-")
input_2 = input("Enter the input 2:-")

print(f"",input_1, "==", input_2, "and", input_1, ">=", input_2, "\n", (input_1 == input_2), "and", (input_1 >= input_2))
print("",input_1 == input_2 and input_1 >= input_2)

print(f"",input_1, "==", input_2, "or", input_1, "<=", input_2, "\n", (input_1 == input_2), "or", (input_1 <= input_2))
print("",input_1 == input_2 or input_1 <= input_2)

print(f"not",input_1, "==", input_2, "or", input_1, "<=", input_2, "\n", (input_1 == input_2), "or", (input_1 <= input_2))
print("", not(input_1 == input_2 or input_1 <= input_2))