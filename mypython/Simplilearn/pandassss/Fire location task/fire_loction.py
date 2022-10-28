import pandas as pd
import numpy as np

df_fdny = pd.read_csv("FDNY_Firehouse_Listing.csv")
# print(df_fdny.describe)
#
# print(df_fdny.head())
# print(df_fdny.columns)

# create a new data frame with only required columne
anly_df_fndy = df_fdny[['FacilityName', 'FacilityAddress', 'Borough']]
print(anly_df_fndy.shape)
print(anly_df_fndy.describe())
print(anly_df_fndy.head())

print(anly_df_fndy.columns)
print(anly_df_fndy.index)

# count a no. of record
print("\n record\n", anly_df_fndy.count())

# view the datatype
print(anly_df_fndy.dtypes)

# select FDNY information boroughwise
groupby_borough = anly_df_fndy.groupby("Borough")
print("\nFDNY information boroughwise\n", groupby_borough)
print(groupby_borough.size())

# select FDNY information Manhattan
fdny_info_Manhattan = groupby_borough.get_group("Manhattan")
print(fdny_info_Manhattan.shape)


