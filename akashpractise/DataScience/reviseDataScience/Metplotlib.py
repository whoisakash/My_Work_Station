from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# x = np.arange(1,11)
# y1 = 2 * x
# y2 = 3 * x
# plt.plot(x, y1, color = "blue", linewidth = 2, linestyle = ":")
# plt.plot(x, y2, color = "red", linewidth = 2, linestyle = ":")
# plt.title("Line Plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid(True)
# plt.show()

# bar plot

# student = {"Sem":30, "Bob":20, "Julia":50}
# names = list(student.keys())
# marks = list(student.values())
# plt.bar(names, marks, color = ["Red", "blue", "yellow"])
# plt.title("Marks of student")
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.grid(True)
# plt.show()

# scatter plot

# x = [2, 5, 6, 8, 4]
# y1 = [4, 7, 6, 2, 8]
# y2 = [2, 5, 8, 7, 9]
#
# plt.scatter(x, y1)
# plt.scatter(x, y2)
# plt.grid(True)
# plt.show()

# histrogram
# iris = pd.read_csv("iris.csv")
# print(iris.head())
# plt.hist(iris["Sepal.Width"])
# plt.show()

# iris.boxplot(column="Petal.Width", by= "Species")
# plt.show()

# sns.boxplot(x=iris["Species"], y=iris["Sepal.Length"])
# plt.show()

fruits = ["apple", "mango", "orange", "banana"]
cost = [50, 90, 40, 30]
plt.figure(figsize=(10, 10))
plt.pie(cost, labels=fruits, autopct="%0.2f%%", shadow=True)
plt.show()
