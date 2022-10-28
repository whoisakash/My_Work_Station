import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# read csv file
data = pd.read_csv("covid_record.csv")
# print(data)
# print(data.max())
# print(data.min())

# print(data.head())
data1 = data.drop(["Date", "State"], axis=1)
# data1 = data.drop(["State"], axis=1)

# print(data1)
# print("\nMax Deaths \n",data1.max())

# print(data1.loc[0,"Deaths"])
# print(data1.iloc[0,0:2])

'''Sorting table as per column'''
# sort_data = data1.sort_values(by='Deaths')
# print("Sortind table\n",sort_data.head())

# sort_data.to_csv("Deathwise.csv",index_label=False)# make csv
# Deaths_sort = pd.read_csv("Deathwise.csv")
# print("\nDeathwise.csv file\n",Deaths_sort.head())

'''Count table data as per column'''
# count_data = data["Region"].value_counts()
# count_data1 = data["Date"].value_counts()
# print(count_data,"\n\n",count_data1)

'''Add Deaths rate column'''
# data["Death Rate(%)"] = (data["Deaths"]/data["Confirmed"])*100
# data["Recover Rate(%)"] = (data["Recovered"]/data["Confirmed"])*100
# print("\nNew column Added\n", data.drop(["Date", "State"], axis=1), data.value_counts(["Death Rate(%)"]))

'''Find Region Where Maximum Deaths'''
# data1 = data.drop(["Date","State"],axis=1)
# print(data1)
# print("\nMax. Deaths")
# i=0
# while True:
#     if data1.loc[i,"Deaths"] == 27682:
#         print(data1.iloc[i, 0:])
#         break
#     i= i+1
# print()

'''Find Region Where Min Deaths'''
# data1 = data.drop(["Date", "State"], axis=1)
# print(data1)
# print("\nMin. Deaths")


'''Region have 0 deaths'''
i=0
a=[]
while i <= 320:
    if data1.loc[i, "Deaths"] == 0:
        # a=(data1.drop([i] , axis=0))
        a.append(data1.loc[i, "Region"])
    i = i + 1
print("Region 0 death Rate\n", a)
print(len(a))


# i=0
# while i <= 320:
#     if data1.loc[i, "Deaths"] != 0:
#         opt = data1.drop([i], axis=0)
#     i += 1
# print(opt)

# data2 = data1.drop([0,2,5] , axis=0)
# print(data2.head(5))
# print("Region 0 death Rate\n", a)
# print(data2)


null_data = data[data['State'].isna()]
# print(null_data)

all_null = data[data.isna().any(axis=1)]
print(all_null)