import numpy as np
import pandas as pd

dict={
    "name":['Harry','Rohan','Shivam','Rohan'],
    "toy":[np.nan,"Top","Gun","Top"],
    "born":['Rampur','Kolkatta','Barailly','Agra']
}
'''creat a dataframe from row data'''
mfg =pd.DataFrame(dict)

# print(mfg.dropna(how='all',axis=1))
'''last Duplicat keep as it is'''
# mfg1 = (mfg.drop_duplicates(subset=['name'],keep='last'))
'''index reset'''
# print(mfg1.reset_index(drop=True))
# print(mfg)
# shape= mfg.shape
# info= mfg.info()

value_count= mfg["name"].value_counts(dropna=False)
print(value_count)