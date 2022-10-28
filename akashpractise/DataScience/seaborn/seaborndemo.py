import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

fmri = sns.load_dataset("fmri")
print(fmri)
plt.figure(11,figsize=(6,4))
sns.lineplot(x="timepoint", y="signal", data=fmri)
plt.show()