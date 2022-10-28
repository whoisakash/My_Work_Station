'''Problem Statement
The dataset you are going to use in this practice is the famous Iris data
set. The dataset consists of 150 records of the lris plant with four features:
"sepal-length", "sepal-width", "petal-length", and "petal-width". All these
features are numeric. The records have been classified into one of the three
classes, that is, "Iris-setosa", "Iris-versicolor", or "Iris-verginica"
You are supposed to reduce the number of variables by merging correlated
variables and extracting the most important features from the dataset that
are responsible for maximum variance in the output.'''

import pandas as pd
import sklearn
from sklearn.datasets import load_iris

data= load_iris()

x= data.data
y= data.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=1)

# print(x_train.shape)
# print(x_test.shape)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
print(lr.fit(x_train, y_train))

y_predict=lr.predict(x_test)
print(y_predict)

from sklearn.metrics import accuracy_score
accuracy =accuracy_score(y_predict, y_test)
print(accuracy)

from sklearn.decomposition import PCA
sklearn_pca = PCA(n_components=0.98)
sklearn_pca.fit(x_train)

print(sklearn_pca)

x_train_transformed= sklearn_pca.transform(x_train)
print(x_train_transformed.shape)
print(x_train.shape)

x_test_transformed = sklearn_pca.transform(x_test)

lr =LogisticRegression(penalty="l1")
lr.fit(x_train_transformed, y_train)
y_predict= accuracy_score(x_test_transformed)

accuracy = accuracy_score(y_predict, y_test)
print(accuracy)