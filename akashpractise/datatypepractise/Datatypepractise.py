'''Mainly 5 type of data
 1) Number :- int, float, complex
 2) Sequence :- str, list, tuple
 3) Boolean True and False
 4) Dictionary
 5) Set'''

# Keywords
# import keyword
#
# print(keyword.kwlist)

# 1)Number datatype
# int1 = 23
# print(type(int1))
#
# float_type = 20.12
# # '''Float type'''
# print(type(float_type))
#
# complex_type = 2+3j
# # '''complex type'''
# print(type(complex_type))
#
#print("\nPtactise For Number datatype")
# inp2 = 2 + 3j
#inp1 = input("Write number :-")
#print(inp1)
#print(type(inp1)) # problem at print type

# 2) sequence datatype
# print("\nPtactise For Sequence(STRING) datatype")
# str1 = input("Hello student, How r u ?\n Says:-")
# print(str1,type(str1))

# print("\nPtactise For Sequence(LIST) datatype")
# list1 = ["Sahil","Samira","Sumit","Shruti"]
# print(list1)
# etr_data = input("Enten the data in list:- ")
#
# # list1.clear()
# list1.append(etr_data)
# print(list1,type(list1))
#
# data1 = input("\nEnter data for Tuple:-")
# tup1 = ["Akash", "Aarohi", "Ansh", "Akshara", data1]
# print(tup1,"\n",type(tup1))
# data_remove = input("Enter Remove data from  Tuple:-")
# print(tup1.remove(data_remove),tup1)

# print("\nPtactise For Sequence(TUPLE) datatype")
# data2 = input("Enter data for Tuple:-")
# tuple1 = ["Akash", "Aarohi", "Ansh", "Akshara", data2]
# print(tuple1,"\n",type(tuple1))

# 3) Boolean
# print("\nPtactise For Boolean datatype\n")
# _bool_ = (2>4)
# print(type(_bool_), _bool_)
# print("\nCheck data1 is greater then data2.")
# num = input("Enter the data1:- ")
# num1 = input("Enter the data2:- ")
# _bool_1 = num>num1
# print(type(_bool_1), _bool_1)

# 4) Dictionary
print("\nPtactise For Dictionary datatype")
staff_dic = {"Hardik":"Manager","Shivi":"Assistant manager","Piyush":"Programmer",
              "Mansi":"Quality Analyst"}
print(staff_dic,type(staff_dic))
print("\nAdd new mamber in Staff list ")
new_member_name = str(input("Name:- "))
new_member_role = str(input("Member Role :-"))
staff_dic[new_member_name] = new_member_role
print(staff_dic,type(staff_dic))
print(staff_dic["Hardik"])
# print(staff_dic.keys())
# print(staff_dic.values())
# get_role_info = input("\nEnter Name for role information :- ")
# print(get_role_info,"is",staff_dic.get(get_role_info))

# 5)Set
# set1 = {2,6,5,7,3,8,1}
# print(set1,type(set1))
# add_set_data = input("Add data :- ")
# set1.add(add_set_data)
# print(set1,type(set1))

