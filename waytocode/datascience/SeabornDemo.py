import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# fmri = sns.load_dataset("fmri")
# print(fmri)
# sns.lineplot(x='timepoint', y='signal', data=fmri)
# plt.show()


# Grouping data

# fmri = sns.load_dataset("fmri")
# print(fmri)
# sns.lineplot(x='timepoint', y='signal', data=fmri, hue='region')
# plt.show()

# style arguement

# fmri = sns.load_dataset("fmri")
# print(fmri)
# sns.lineplot(x='timepoint', y='signal', data=fmri, hue='event', style='event')
# plt.show()


# markers arguement

# fmri = sns.load_dataset("fmri")
# print(fmri)
# sns.lineplot(x='timepoint', y='signal', data=fmri, hue='event', style='event', markers=True)
# plt.show()


# pandas dataset

# data = pd.read_csv('cricketer.csv')
# sns.barplot(x='Total Runs', y='Age', data=data)
# plt.show()

# data = pd.read_csv('cricketer.csv')
# sns.barplot(x='Total Runs', y='Age', data=data, hue='Fullname')
# plt.show()

# Palette arg : 'Blues_d or rocket or vlag

# data = pd.read_csv('cricketer.csv')
# sns.barplot(x='Total Runs', y='Age', data=data, hue='Fullname', palette='Blues_d')
# plt.show()

# data = pd.read_csv('cricketer.csv')
# sns.barplot(x='Total Runs', y='Age', data=data, hue='Fullname', color='red')
# plt.show()

# scatterplot

# data = pd.read_csv('cricketer.csv')
# sns.scatterplot(x='Total Runs', y='Age', data=data, hue='Fullname', style='Fullname')
# plt.show()


# histogram

# data = pd.read_csv('cricketer.csv')
# sns.histplot(data['Total Runs'])
# sns.distplot(data['Total Runs'])
# plt.show()

# data = pd.read_csv('cricketer.csv')
# # sns.distplot(data['Total Runs'], hist=False )
# sns.distplot(data['Total Runs'], vertical=True)
# plt.show()

# kde=False  ---To remove the curve


# Jointplot

# data = pd.read_csv('cricketer.csv')
# # sns.jointplot(x='Total Runs', y='Age', data=data)
# # Regressionplot
# sns.jointplot(x='Total Runs', y='Age', data=data, kind='reg')
# plt.show()





