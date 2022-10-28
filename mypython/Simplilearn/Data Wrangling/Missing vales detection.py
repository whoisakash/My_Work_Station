import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# df =pd.read_csv("class_grades.csv")
#
# print(df.isna().any())
# plt.boxplot(x=df["Assignment"])
# plt.show()

world cup=['Team': ['West Indies', 'West indies ',
'India', 'Australia', 'Pakistan', 'Sri
'Australia', 'Austral ia', 'Australia', ' Insia',
'Australia' 1, 'Rank' : [7,7,2,1,6, 4,1,1,1,2,11,
'Year': [1975,1979, 1983,1987, 1992, 1996,1999, 2003,
2007,2011,2015]
Lanka',
df-pd. DataTrame (world_cup)
print (df.groupby (['Team', 'Rank']).groups)