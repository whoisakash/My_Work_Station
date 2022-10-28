class_A = ["Bramha", "Vishnu", "Mahesh"]
class_B = ["Saraswati", "Lakshmi", "Parvati"]

print(class_A, class_B)
_name = input("\nEnter Name for check Person is in class B? :- ")
print(_name in class_B)

_name1 = input("\nEnter Name for check Person is not in class A? :- ")
print(_name1 not in class_A)