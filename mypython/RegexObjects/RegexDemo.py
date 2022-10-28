import re

#Regex Match objects
my_text = "Tutorial from Great Learning"
# a= re.search("fr",my_text)
# a= re.search("aa",my_text)
a= re.search("zip",my_text)
# print(a)
# print(my_text[9:11],"see")

#Regex Match methods Hands-on
# print(a.span(),"location of search item")

# print(a.string)#get full string of search item

# print(a.group())#print search item

# Regex functions: re./findall(), search(), split(), sub()
my_txet1= "My name is akash, i have bananaes"
# a= re.findall("a",my_txet1)# find how many time in serch data

# a= re.split("na",my_txet1)#split data at data match

a= re.sub("na","bc",my_txet1)#exchange element and reture update string
print(a)
