import matplotlib.pyplot as plt
import seaborn as sns

flight_dataa = sns.load_dataset("flights")

# print(flight_dataa.head())
# print(flight_dataa.tail())

flight_dataa = flight_dataa.pivot("month", "year", "passengers")
print(flight_dataa)
sns.heatmap(flight_dataa)
plt.show()

