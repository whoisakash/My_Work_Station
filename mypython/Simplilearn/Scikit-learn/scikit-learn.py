'''Problem Statement
You have been provided with a dataset that contains the costs of advertising on different
media channels and the corresponding sales of XY2 firm. Evaluate the dataset to:
1. Find the features or media channels used by the firm
2. Find the sales figures for each channel
3. Create a model to predict the sales outcome
4. Split it into training and testing datasets for the model
5. Calculate the mean squared error (MSE)'''

import pandas as pd

df_adv_data= pd.read_csv("Advertising.csv", index_col=0)

print(df_adv_data.head())

print(df_adv_data.shape)

print(df_adv_data.columns)

# Create a feature object from the columns
x_feature = df_adv_data[['TV', 'Radio', 'Newspaper']]
# print(x_feature.head())

y_targets= df_adv_data[["Sales"]]
# print(y_targets.head())

# Split test and training data
# by default 75% training  data and 25% testing data

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_feature, y_targets, random_state=1)
print("\nx_train\n", x_train.shape)
print("\ny_train\n", y_train.shape)
print("\nx_test\n", x_test.shape)
print("\ny_test\n",y_test.shape)

# linear regration model
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
print(linreg.fit(x_train, y_train))

# print the intercept and coefficients
print(linreg.intercept_)
print(linreg.coef_)

# prediction
y_pred = linreg.predict(x_test)
print(y_pred)

# learn required libraries for calculating MSE(mean square error)
from sklearn import metrics
import numpy as np

# calculate the mean square error(MSE)
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))