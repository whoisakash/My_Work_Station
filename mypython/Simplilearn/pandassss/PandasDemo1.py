import pandas as pd
import numpy as np

data = pd.read_csv("covid_record.csv")

print(data.shape) #(321, 6)

print(data.head())

print(data.columns)

# create a new data frame with only required columne
analyze_data= data[['State', 'Region', 'Confirmed', 'Deaths', 'Recovered']]
print(type(analyze_data))
print(analyze_data.head())

print("\nReplace all Nan for State with No")
analyze_data["State"].fillna(value="No", axis=0, inplace= True)
print(analyze_data.head())
print(analyze_data.shape)

print("\nremove all NO state in database")
final_data = analyze_data.dropna(subset=["State"], axis=0)
print(final_data)