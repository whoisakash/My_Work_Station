import numpy as np
import pandas as pd

dict={
    "name":['Harry','Rohan','Shivam','Shubh'],
    "marks":[92, 34, 24, 17],
    "city":['Rampur','Kolkatta','Barailly','Agra']
}
'''creat a dataframe from row data'''
df =pd.DataFrame(dict)
# print(df)

'''creat a csv file and put this datafream in this file
hrea index = false use for 0,1,2,3 inexing number remove
'''
df.to_csv("Marksheet.csv",index=False)

'''(.head) for top to specific row'''
# print(df.head(2))
'''(.tail) for last to specific row'''
# print(df.tail(),"\n")
'''.head for top to specific row'''
# print(df.describe())

marksheet = pd.read_csv("Marksheet.csv")
print(marksheet)

# marksheet["marks"][3]=71
# print(marksheet,)

# marksheet.to_csv("Marksheet.csv")
''' for perticular rcolumna and all row{ .loc[row, coulmmn]}'''
print(marksheet.loc[:,("name","city","marks")])
print(marksheet.loc[(2,3),:])

'''compelx shee to find data from conditon'''
print(marksheet.loc[(marksheet["marks"]<50) & (marksheet["marks"]>20)])