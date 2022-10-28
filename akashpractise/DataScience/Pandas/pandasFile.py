import numpy as np

import pandas as pd
# data = pd.read_csv("Demodata.csv")
# print(data)
# f_data= data.iloc[[0,2],[0,2]]
# f_data= data.iloc[1:2,2:3]
# print("\n",f_data)

# Ro = csv.reader("Demodata.csv",dialect='')
# print(Ro)

# dt = pd.Series({"a":1,"b":2,"c":3,"d":4})
# dt1 = pd.Series({"a":1,"b":2,"c":3,"d":4})
# print(dt-dt1)

# Create Data Frame

df = pd.DataFrame({'User': ['Abhishek', 'Akash', 'Gautam','Amish'], 'Role': ['Pyt', 'C++', 'Java','HTML'],
                   'Days':[25,30,40,15]})
# print(df.tail(1))
# print(df.head(1))
# print(df.shape)
# print(df.describe())

# head(), shape(), describe(), tail()
df = pd.read_csv('marksheet.csv')
print(df)
# df1 = pd.DataFrame(df,index=[1,0,3])
# print(df1)
'''how to remove index in '''
# print(df.loc[0:8,["Name","Gujrati","Math","Science"]])

print(df.drop(["Gujrati"],axis=1))

'''
make function whoes work as row calcutaion
1. Find Name and print
2. and range to use value for sum of perticular student
3. name input and total marks as a output
'''
# data = pd.read_csv("marksheet.csv")
#
# find =data.loc[0:8,"Name"]
# print(find)
# take_1 = str(input("Enter Name of Student:- "))
# take_n = take_1.capitalize()
# # print(take_n)
# for i in find:
#     if i == take_n:
#         print(i,"finded")
#         break
#     else:
#         print(take_n,"is not in list")

# def total_marks():

