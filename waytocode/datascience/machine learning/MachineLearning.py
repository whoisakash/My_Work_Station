# Classification, Regression and Clustering

# classification : the data which are classified
# regression : the data which is numeric
# clustering : the data hierarchical data

# Types of ML : Supervised and Unsupervised Learning

# Supervised Learning
# Basically two of variables : Independent and Dependent.
# Independent variables : the variables defined by user itself.

# usernum = input("Enter number : ")
# print(usernum)

# Types of Supervised Learning : Regression and clasiffication


# Unsupervised Learning
# In this we dont have labels on data.
# Its use clustering algorithms.
# Types of clusterning : High Interclustering Similarities and High Interclustering dissimilarities
import csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv("grading_system.csv")

print(data.columns)
#
# sns.scatterplot(x="Assignment", y="Tutorial", data=data, hue="Final")
# plt.show()

x = data[['Assignment']]
y = data[['Tutorial']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# print(x_train.shape)
# print(x_test.shape)

# lr = LinearRegression()
# lr.fit(x_train, y_train)

df_class_gread = pd.read_csv("grading.csv")

# print(df_class_gread.head())

# analy_df_class = df_class_gread["Assignment"].fillna(value="0", axis=0, inplace=True)
df_class_gread["Assignment"].fillna(value="0", axis=0, inplace=True)
df_class_gread["Tutorial"].fillna(value="0", axis=0, inplace=True)
df_class_gread["Midterm"].fillna(value="0", axis=0, inplace=True)
df_class_gread["TakeHome"].fillna(value="0", axis=0, inplace=True)
df_class_gread["Final"].fillna(value="0", axis=0, inplace=True)
print(df_class_gread.head())

# with open('NON-NUN_Class.csv', 'w') as csvFile:
#     for i in csvFile:
#         writer = csv.DictWriter(csvFile,fieldnames="")
#
#         writer.writerows(df_class_gread)
#
# print("Data Inserted")

df_class_gread.to_csv("final_class_gread.csv", index=False)
data = pd.read_csv("final_class_gread.csv")
