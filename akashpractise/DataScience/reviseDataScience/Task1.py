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

# Create 3X4 numpy array
my_data = np.array([[25,63,87,45],[87,58,65,12],[58,25,33,87]])
# print(my_data.shape)

data_column_name = ["Eleaor","Childi","Tahani","Jason"]
my_dataframe = pd.DataFrame(data=my_data,columns=data_column_name)
print(my_dataframe)

print("\n",my_dataframe.iloc[1,0],"Value of row #1 of the Elanor column")

my_dataframe["Janet"]= my_dataframe["Tahani"] + my_dataframe["Jason"]

print(my_dataframe)