'''
1.Create an 3x4 (3 Rows x 4 columns) pandas DataFrame in which the columns are named
Eleanor, Childi, Tahani And Jason. populate each of the 12 cells in the DataFrame with a random
integer between 0 and 100, inclusive.

2. Output the following:
--The Entrie Dataframe
-- The value in the cell of the row #1 of the Elanor column

3. Create A 5th column Named Janet, which  is populated with the row-by-row sum of
Tahani and Jason
'''
import pandas as pd
import numpy as np

data_column_name = ["Eleaor","Childi","Tahani","Jason"]

data = np.random.randint(low = 0,high = 100,size=(3,4))

df = pd.DataFrame(data=data,columns=data_column_name)
print(df)

print("value in the cell of the row #1 of the Elanor column")
print(df["Eleaor"][1])

print("Create A 5th column Named Janet and\nput value sum of Tahani and Jason")
df["Janet"] = df["Tahani"]+df["Jason"]
print(df)

'''Copy method:
1. referencing: assign dataframe to a new variable,then any one change can reflected in the other
2. Copying: pd.DataFrame.copy method. changing in original DataFrame or to the Copy will not be reflected in the other'''

print("\nExperiment with a reference: ")
referance_to_df = df

# "Print The starting value of particular cell"
print("Starting value of df: %d"% df["Jason"][1])
print("Starting value of referance_to_df: %d"% referance_to_df["Jason"][1])

# Modify a cell in df
df.at[1,"Jason"] = df["Jason"][1] + 5
print("Update df: %d" %df["Jason"][1])
print("Updating value of referance_to_df: %d"% referance_to_df["Jason"][1])




# Creat and populate 5x2 numpy array.
my_data = np.array([[5,2],[6,7],[7,3],[8,4],[6,1]])

# Creat a python list and hold the name of the two columns.
my_column_name = ["Temperture","Activity"]

# create dataframe.
my_dataframe = pd.DataFrame(data=my_data,columns=my_column_name)

#2. Create a true copy of my_dataframe
print("\nExperiment with a true copy: ")
copy_of_my_dataframe = my_dataframe.copy()

# Print the starting value of a particular cell
print("Starting Value of my_dataframe: %d" % my_dataframe["Activity"][1])
print("Starting Value of copy_of_my_dataframe: %d" % copy_of_my_dataframe["Activity"][1])

# Modify a cell in df
my_dataframe.at[1,"Activity"] = my_dataframe["Activity"][1] + 5
print("Update my_dataframe: %d" %my_dataframe["Activity"][1])
print("Updating value of copy_of_my_dataframe: %d" %copy_of_my_dataframe["Activity"][1])
