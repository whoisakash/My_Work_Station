list1 = ["Abhi", "Abhimanyu", "Arjun", "Aklavya"]
list2 = ["Karn", "Krishna", "Kauravas", "Kashyap"]

list3 = list1
list4 = list2

print("List1",list1)
print("List2",list2)
print("List3",list3)
print("List4",list4)

print("\nlist3 is list1 -", list3 is list1)
print("list3 is list2 -", list3 is list2)
print("list1 is list2 -", list1 is list2)
print("list1 is list3 -", list1 is list3)
print("list2 is list4 -", list2 is list4)
print("list2 is list1 -", list2 is list1)
print("list4 is list2 -", list4 is list2)
print("list4 is list1 -", list4 is list1)