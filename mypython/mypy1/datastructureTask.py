month = ["January","February","March","April","May"]
expenses = [2200,2350,2600,2130,2190]
dict_exp = {"January":2200,"February":2350,"March":2600,"April":2130,"May":2190}

a= (dict_exp["January"])
b= (dict_exp["February"])
e= (dict_exp["March"])

while True:
    if a > b:
        c=(a - b)
        break
    elif a < b:
        c=(b - a)
        break
    else:
        print("both are same")
        break
print(c)
"""How could get ans when value doest match single time"""
for i in dict_exp:
    if (dict_exp[i]) == 9000:
        print(i, "Yes Found")
        # print("month expenses")
    else:
        print(i, "Not Found")

'''Quqterly Expenses'''
print(a,b,e)
qtr_exp= a+b+e
print("ans3",a,b,e,"Total",qtr_exp)

'''Add june expenses'''
dict_exp["June"]= 1980
print("ans4",dict_exp)

'''April month return item to change expenses'''
print(dict_exp["April"])
dict_exp["April"]-=200
print(dict_exp["April"])





