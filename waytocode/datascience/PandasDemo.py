import pandas as pd

# single dimens labeled array

# dt = pd.Series(['a', 'b', 'c', 'd'])
# print(dt)
# print(type(dt))


# change in index

# data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(data)


# dictionary single dimens

# data = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
# print(data)

# dictionaary change in index

# data = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4}, index=['c', 'd', 'b'])
# print(data)


# Extract single value

# data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
# extr = data[6]
# print(extr)


# Extract from back value

# data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
# extr = data[-6:]
# print(extr)


# Extract sequence value

# data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
# extr = data[1:6]
# print(extr)


# Basic Arithmatic Operation

# data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
# data1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
# addData = data + data1
# # addData = data + 10
# print(addData)


# Create Data Frame

# df = pd.DataFrame({'User': ['Abhishek', 'Akash', 'Gautam'], 'Role': ['Pyt', 'C++', 'Java']})
# print(df)

# head(), shape(), describe(), tail()

# iloc

# data = pd.read_csv('pandaswork.csv')
# opt = data.iloc[3:4, 2:3]
# print(opt)


# write excel file


# df = pd.DataFrame({'User': ['Abhishek', 'Akash', 'Gautam'], 'Role': ['Pyt', 'C++', 'Java']})
# print(df)
#
# df.to_excel('pandas.xlsx', index=False, header=False)


# loc

# data = pd.read_csv('pandaswork.csv')
# opt = data.loc[1:3, ('email', 'number')]
# print(opt)

# dropping column

# data = pd.read_csv('pandaswork.csv')
# opt = data.drop('fullname', axis=1)
# print(opt)


# dropping row
#
# data = pd.read_csv('pandaswork.csv')
# opt = data.drop([1, 3], axis=0)
# print(opt)

# task
# mean(), min(), median() and max()

# self-made function

# data = pd.read_csv('pandaswork.csv')
#
# def addData(num):
#     return num + 2
#
# data1 = data[['number']].apply(addData)
#
# print(data1)


# value_count and sort_value

# data = pd.read_csv('pandaswork.csv')
#
# # dt = data['number'].value_counts(4)
# dt = data.sort_values(by='fullname')
# print(dt)












