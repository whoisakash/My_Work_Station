import pandas as pd
import numpy as np

# Create DataFrame from list
# olympic_data_list = {"Host city": ["London", "Beijing", "Athens", "Sydney", "Atlanta"],
#                      "Year": [2012, 2008, 2004, 2000, 1996],
#                      "No. of Participating Country": [205, 204, 201, 200, 197]}
#
# df_of_data = pd.DataFrame(olympic_data_list)
# print(df_of_data)
# print(df_of_data.describe)

# Create DataFrame from Dict of series
oly_series_parti = pd.Series([205, 204, 201, 200, 197], index=[2012, 2008, 2004, 2000, 1996])
oly_series_country = pd.Series(["London", "Beijing", "Athens", "Sydney", "Atlanta"], index=[2012, 2008, 2004, 2000, 1996])

df1 = pd.DataFrame({"No. of Participating Country":oly_series_parti,
                    "Host Cities":oly_series_country})
# print(df1)
# print(df1.info())

# Create DataFrame from ndarray
# np_array = np.array([205, 204, 201, 200, 197])
# dict_ndarray = {"year":np_array}
# df_ndarray = pd.DataFrame(dict_ndarray)
# print(df_ndarray)

# Create DataFrame from Dataframe
df_from_df = pd.DataFrame(df1)
print(df_from_df)
print(df1)
