import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
df_auto_dataset = pd.read_csv("auto-mpg.csv")
print(df_auto_dataset.head())
print(df_auto_dataset.columns)

# Write a user define function for origin
# 1-USA, 2-Europe, 3-Axis
def origin(num):
    if num==1:
        return("USA")
    elif num==2:
        return("Europe")
    else:
        return("Asia")

# Use apply the function
df_auto_dataset["origin"]= df_auto_dataset["origin"].apply(origin,)

# view 30 data points after applying the user defined function to data set
print(df_auto_dataset.head(30))

# draw the pair plot using sns for mpg, weight, orign and with hue origin, set the size to 4
# note: hue is a variable for dataset  to map plot aspects to differnt colors

sns.pairplot(df_auto_dataset[["mpg", "weight", "origin"]], hue="origin", size=4)
plt.show()