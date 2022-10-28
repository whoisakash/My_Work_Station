import pandas as pd
import numpy as np

data = pd.read_csv("whether_report.csv")
print(data)
# print(data.describe())
# print(data.max())

'''1. Find all the unique Wind Speed values in the data.
Ans: 34 no of unique speed '''
unq_wind = data["Wind Speed_km/h"].value_counts()
# print(len(unq_wind))
# unq_wind.to_csv("Unique Speed.csv")
# unq_file = pd.read_csv("Unique Speed.csv")
# print(unq_file)


'''2. Find the no. of times when the Weather is exactly clear.
Ans: 1326 times when weather is clear'''
weather_cond = data["Weather"].value_counts()
print(len(weather_cond), "type of Weather Condition")
print(weather_cond, weather_cond.sort_values())
print("\n")


'''3. Find the no. of times when the wind speed was exactly 4kmph.
Ans: 474 time '''
# print(len(unq_wind))
# print(unq_wind)

'''4. Find out all the null values in the data.
Ans. No Null values '''
all_null = data[data.isna().any(axis=1)]
print(all_null)

# For each Column
# null_data = data[data["Temp_C"].isna()]
# print(null_data)

'''5. Rename the column name Weather of the dataframe to Weather Condition.
'''
# dict = {"Date/Time": "Date/Time", "Temp_C": "Temp_C", 'Dew Point Temp_C': 'Dew Point Temp_C',
#         'Rel Hum_%': 'Rel Hum_%', 'Wind Speed_km/h': 'Wind Speed_km/h',
#         'Visibility_km': 'Visibility_km', 'Press_kPa': 'Press_kPa', 'Weather': 'Weather Condition'}
dict = {'Weather': 'Weather Condition'}
# print("\nRename done\n")
data.rename(columns=dict, inplace=True)
# print(data)

'''6. What is the mean Visibility.
Ans. Visibility_km - 27.66447'''
# print("mean Visibility",data['Visibility_km'].mean())


'''7. What is the standard deviation of Pressure in this data.'''
# print("standard deviation of Pressure", data["Press_kPa"].std())


'''8. What is the Variance of Relative Humidity in this data.'''
# print("Variance of Relative Humidity", np.var(data['Rel Hum_%']))

'''9. Find all instances when snow was recorded.'''
no = []
condition = "Snow"
for i in range(0, 8784):
    if condition in data.loc[i, "Weather Condition"]:
        no.append(data.iloc[i, 0:])
print("For loop\n", len(no), no[0:3])
df = pd.DataFrame(no, columns=["Date/Time", "Temp_C", "Dew Point Temp_C", "Rel Hum_%", "Wind Speed_km/h", "Visibility_km", "Press_kPa", "Weather Condition"])
print(df)

# i = 0
# a = []
# s = "Snow"
# while True: #i <= 8785
#     if s in data.loc[i, "Weather Condition"]:
#         a.append(data.drop([i], axis=0))
#         # a.append(data.loc[i, "Date/Time"])
#     i += 1
# print("Snow Fall Day\n", a)
# print(a

# d1 = data.loc[2, "Date/Time"]
# print(d1)
# abg = data.loc[2, "Weather Condition"]
# print(abg)
# a1 = "Fog" in data.loc[2, "Weather Condition"]
# print(a1)

'''10. find all instances when wind speed is above 24 and visibility is 25.'''
num = []
for i in range(0, 8784):
    if (data.loc[i, "Wind Speed_km/h"] > 24) and (data.loc[i, "Visibility_km"] > 25):
        num.append(data.iloc[i, 0:])
# print("\nwind speed is above 24 and visibility is 25\n", len(num), num[0])
df1 = pd.DataFrame(num, columns=["Date/Time", "Temp_C", "Dew Point Temp_C", "Rel Hum_%", "Wind Speed_km/h", "Visibility_km", "Press_kPa", "Weather Condition"])
# print(df1)

# print(df1.loc[0:, ["Wind Speed_km/h", "Visibility_km"]])

'''11. What is the mean value of each column against each weather condition.'''
men_value = data.mean()
# print("\n", men_value)

'''12. What is the minimum and maximum value of each column against each weather condition.'''
maxi_value = data.max()
# print("\n Maximum Value \n", maxi_value)

'''13. Show all the records where weather condition is fog.'''
no2 = []
condition1 = "Fog"
for i in range(0, 8784):
    if condition1 in data.loc[i, "Weather Condition"]:
        no2.append(data.iloc[i, 0:])
# print("weather condition is fog\n", len(no2), no2[0:3])
df2 = pd.DataFrame(no, columns=["Date/Time", "Temp_C", "Dew Point Temp_C", "Rel Hum_%", "Wind Speed_km/h", "Visibility_km", "Press_kPa", "Weather Condition"])
print(df2)

'''14. Find all the instance when weather is clear or visibility is above 40.'''
num3 = []
for i in range(0, 8784):
    if ("Clear" in data.loc[i, "Weather Condition"]) or (data.loc[i, "Visibility_km"] > 40):
        num3.append(data.iloc[i, 0:])
# print("\nwind speed is above 24 and visibility is 25\n", len(num3), num3[0:6])
df3 = pd.DataFrame(num3, columns=["Date/Time", "Temp_C", "Dew Point Temp_C", "Rel Hum_%", "Wind Speed_km/h", "Visibility_km", "Press_kPa", "Weather Condition"])
print(df3.iloc[0:11,[4,7]])

'''15. Find all the instance when weather is clear or relative humidity is above 50.'''
num4 = []
for i in range(0, 8784):
    if ("Clear" in data.loc[i, "Weather Condition"]) or (data.loc[i, "Rel Hum_%"] > 50):
        num4.append(data.iloc[i, 0:])
# print("\nweather is clear or relative humidity is above 50\n", len(num4), num4[0:6])
df4 = pd.DataFrame(num3, columns=["Date/Time", "Temp_C", "Dew Point Temp_C", "Rel Hum_%", "Wind Speed_km/h", "Visibility_km", "Press_kPa", "Weather Condition"])
# print(df4.iloc[0:11,[3,7]])