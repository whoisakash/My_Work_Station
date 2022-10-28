import pandas as pd
import numpy as np

# Creat and populate 5x2 numpy array.
my_data = np.array([[5,2],[6,7],[7,3],[8,4],[6,1]])

# Creat a python list and hold the name of the two columns.
my_column_name = ["Temperture","Activity"]

# create dataframe.
my_dataframe = pd.DataFrame(data=my_data,columns=my_column_name)

# Print the entire Dataframe
# print(my_dataframe)

# Create a new column named adjusted.
# my_dataframe["Position"] = my_dataframe["Activity"] + 2

# Print the entire Dataframe
# print(my_dataframe)

'''Specifying A subset of a dataframe'''
# print("Rows #0,#1,and #2")
# print(my_dataframe.head(3),"\n")

# print("Rows #2")
# perticular row details
# print(my_dataframe.iloc[2])
# as per tabular row
# print(my_dataframe.iloc[[2]])

# print("Rows #1,#2,and #4")
# print(my_dataframe[1:4])

# print("column 'Temperture': ")
# print(my_dataframe["Temperture"])

n1 = np.array([10,20,30,40,50])
n2 = np.array([60,50,40,70,80])
# print("vertical array:  vstack()")
# print(np.vstack((n2,n1)))
#
# print("horizontal array: hstack()")
# print(np.hstack((n2,n1)))
#
# print("\ncolumn_stack()")
# print(np.column_stack((n2,n1)))

# interset data show
print(np.intersect1d(n1,n2))


