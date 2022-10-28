'''Problem Statement
You are a public-school administrator. Some schools in your state of Tennessee are
performing below average academically. Your superintendent seems to be under
pressure from frustrated parents and the voters have appoached you with the task of
finding out why these schools are underperforming.
Now, to improve school performance, you need to learn more about these schools
and their students, just as a business needs to understand its own strengths and
weaknesses and its customers. The data includes various demographics, the school
faculty, and income variables.
This can be achieved using exploratory data analysis techniques which further
include:
Reading the data in pandas data frame
Describing the data to find more details
Finding the correlation between 'reduced_lunch' and 'school_rating'''

import pandas as pd
df = pd.read_csv("school.csv")
print(df.describe())
print(df.columns)

# phase 2
a1=df[['reduced_lunch', 'school_rating']].groupby(['school_rating']).describe().unstack()
print(a1)

a2=df[['reduced_lunch', 'school_rating']].corr()
print(a2)