import re

# str = "developer is my name"
#
# matches = re.findall("developer", str)
# print(matches)
# print(type(matches))

# name = input("Enter Name : ")
# matches = "abhi"
#
# if re.findall(name, matches):
#     print(name)
#
# else:
#     print("Data not matched")

list = "gautama"

matches = re.search("a", list)
print(matches)
