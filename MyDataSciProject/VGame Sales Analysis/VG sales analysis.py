'''Analyzing sales data for over 16,500 games
 is a very popular problem statement on Kaggle.
You can either solve this problem to find numerous patterns and relationships between factors affecting video game sales, or you can use this dataset to predict future video game sales. So in the section below, I’m going to walk you through how to train a machine learning model for predicting video game sales using Python.'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

vg_sales_data = pd.read_csv("vgsales.csv")
print(vg_sales_data.shape)

print(vg_sales_data.isnull().sum())
vg_sales_data =vg_sales_data.dropna()
print(vg_sales_data)
print(vg_sales_data.columns)

import matplotlib as mpl
game= vg_sales_data.groupby("Genre")["Global_Sales"].count()
print(game)
# s=pd.Series(game)
# print(s.index)

custom_colors= mpl.colors.Normalize(vmin=min(game), vmax=max(game))
colors = [mpl.cm.PuBu(custom_colors(i)) for i in game]

plt.figure(figsize=(7,7))
plt.subplots_adjust(hspace=1)
plt.subplot(2,1,1)


# plt.pie(game, labels=game.index, color=colors)
plt.pie(game, labels=game.index, autopct="%1.1f%%")
central_circle= plt.Circle((0,0), 0.5, color="white")
fig= plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc("font", size=12)

# plt.pie(game, labels=s.index, autopct="%1.1f%%")
plt.title("Top 10 Categories of Game Sold")

'''correlation between the features of this dataset:'''
print(vg_sales_data.corr())
plt.subplot(2, 1, 2)
sns.heatmap(vg_sales_data.corr(), cmap="winter_r")
# plt.show()

'''Sales Predivtion Model'''
x = vg_sales_data[["Rank", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]]
y = vg_sales_data["Global_Sales"]

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain, ytrain)
predictions= model.predict(xtest)
print(predictions.shape)
print(xtest.shape)
print(xtrain.shape)