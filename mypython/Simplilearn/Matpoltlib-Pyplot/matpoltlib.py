from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# load bosten dataset
boston_real_state_data= load_boston()

print(boston_real_state_data.data)
print("\n")
print(boston_real_state_data.taget)

# define x as data and y as target
x_axis = baston_real_state_data.data
y_axis = baston_real_state_data.target

# plot histogram
# style.use("ggplot")
# plt.figure(figsize=(7, 7))
# plt.hist(y_axis, bins=50)
# plt.xlabel("price in 1000s USD")
# plt.ylabel("Number of house")
# plt.show()

# plot scatter plot
style.use("ggplot")
plt.figure(figsize=(7, 7))
plt.scatter(boston_real_state_data.data[:5], boston_real_state_data.target)
plt.ylabel("price in 1000s")
plt.xlabel("number of houses")
plt.show()