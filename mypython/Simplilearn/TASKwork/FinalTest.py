'''IBM is an American MNC operating in around 170 countries with major business vertical as computing, software, and hardware.
Attrition is a major risk to service-providing organizations where trained and experienced people are the assets of the company.
 The organization would like to identify the factors which influence the attrition of employees.

Data Dictionary

Age: Age of employee
Attrition: Employee attrition status
Department: Department of work
DistanceFromHome
Education: 1-Below College; 2- College; 3-Bachelor; 4-Master; 5-Doctor;
EducationField
EnvironmentSatisfaction: 1-Low; 2-Medium; 3-High; 4-Very High;
JobSatisfaction: 1-Low; 2-Medium; 3-High; 4-Very High;
MaritalStatus
MonthlyIncome
NumCompaniesWorked: Number of companies worked prior to IBM
WorkLifeBalance: 1-Bad; 2-Good; 3-Better; 4-Best;
YearsAtCompany: Current years of service in IBM
Analysis Task:
- Import attrition dataset and import libraries such as pandas, matplotlib.pyplot, numpy, and seaborn.
- Exploratory data analysis

Find the age distribution of employees in IBM
Explore attrition by age
Explore data for Left employees
Find out the distribution of employees by the education field
Give a bar chart for the number of married and unmarried employees
- Build up a logistic regression model to predict which employees are likely to attrite.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn


IBM_data = pd.read_csv("IBM Attrition Data.csv")
# print(IBM_data.columns)
# print(IBM_data.head())
# print(IBM_data.shape)

# Make histogram for age
# plt.figure(figsize=(10,9))
# IBM_data["Age"].hist(bins=70)
# plt.title("Employees Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("No. of Employees")
# plt.show()

# Data exploration for Attrition by age
# plt.figure(figsize=(15, 10))
# plt.scatter(IBM_data.Attrition, IBM_data.Age, alpha=.55)
# plt.title("Age Attrition")
# plt.ylabel("Age")
# plt.grid(b=True, which="major", axis="y")
# plt.show()

# explore data for left employees breakdown
# plt.figure(figsize=(5, 5))
# IBM_data.Attrition.value_counts().plot(kind="barh", color="blue", alpha=.65)
# plt.title("Attrition breakdown")
# plt.show()

# explore data for Education Field Distribution
# plt.figure(figsize=(10, 9))
# IBM_data.EducationField.value_counts().plot(kind="barh", color="blue", alpha=.65)
# plt.title("Education Field Distribution")
# plt.show()

# Explore data for Marital Status
# plt.figure(figsize=(8, 6))
# IBM_data.MaritalStatus.value_counts().plot(kind="bar", alpha=.5)
# plt.title("Marital Status")
# plt.show()

# print(IBM_data.describe())
# print(IBM_data.info())
# print(IBM_data.std())
print(IBM_data.columns)

# print(IBM_data.Attrition.value_counts())
# print(IBM_data.Attrition.dtypes)
# print(IBM_data["Attrition"].dtypes)
IBM_data["Attrition"].replace("Yes", 1, inplace=True)
IBM_data["Attrition"].replace("No", 0, inplace=True)

print(IBM_data.Attrition.value_counts())

# building up a logistic regression model
X=IBM_data.drop(["Attrition"], axis=1)
print(X.head())
Y=IBM_data["Attrition"]
print(Y.head())


print(IBM_data.EducationField.value_counts())
IBM_data["EducationField"].replace("Life Sciences",1, inplace=True)
IBM_data["EducationField"].replace("Medical",2, inplace=True)
IBM_data["EducationField"].replace("Marketing",3, inplace=True)
IBM_data["EducationField"].replace("Other",4, inplace=True)
IBM_data["EducationField"].replace("Technical Degree",5, inplace=True)
IBM_data["EducationField"].replace("Human Resources",6  , inplace=True)
