import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import re
# read csv file
data = pd.read_csv("covid_record.csv")
print(data)

# try to find same region
region = data.iloc[[0,50],2]
# region = data.loc[0:,"Region"]
print("REGION data\n",region)
deaths = data.loc[[0,50],"Deaths"]
print("DEATHS data\n",deaths)

# print(type(list(deaths)),type(deaths))
print(list(deaths))

# reg_count= set(region)
# reg_count= list(region)
# reg_count= tuple(region)
# reg_count= {region:deaths}
# print(reg_count)
# print(len(region))# all region are not same

# plot graph Region vs plot
a = list(region)
b = list(deaths)

data = plt.barh(a,b)
print(data)

# plt.scatter(a,b,)
plt.show()


# def find_max():
