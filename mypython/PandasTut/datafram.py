import pandas as pd
import numpy as np

newdf = pd.DataFrame((105,5),index=np.arange(104))
print(newdf)

newdf.head()