import pandas as pd
import numpy as np

# Create a series
# nation = ["India", "Canada", "UK", "USA", "UAE", "China"]
# GDP = [8.0123, 8.2565, 9.1254, 9.2547, 8.2568, 7.5682]
#
# data = pd.Series(GDP, index=(nation))
# print(data)

# Scaler series
# data1 = pd.Series(0, index=[list("abcd")])
# print(data1)

#Accessing Elements in series
# print(data[0])
# print(data[0:])
#
# print("GDP of chine ", data.loc["China"])
#
# print("GDP of 1st nation ", data.iloc[0])

# Vectorized operations

data5 = pd.Series([10, 20, 30, 40], index=[list("adcb")])
data3 = pd.Series([1, 2, 3, 4], index=[list("abcd")])
data4 = pd.Series([10, 20, 30, 40], index=[list("abcd")])
print(data3 + data4)
print(data5 + data3)


data6 = pd.Series([10, 20, 30, 40], index=[list("abef")])
print(data3 + data6)