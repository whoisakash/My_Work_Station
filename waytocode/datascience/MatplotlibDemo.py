from matplotlib import pyplot as plt
from matplotlib import style
from mpl_toolkits import mplot3d
import numpy as np


# Pie, 3d, bar, multiple graph


# Basic Plotting

# data = plt.plot([1, 2, 3, 4, 5], [4, 2, 6, 3, 7])
# print(data)
# plt.show()

# x = [4, 1, 7]
# y = [1, 9, 6]
# plt.plot(x, y)
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.title("Basic Graph Plotting")
# plt.show()


# Colour

# plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'yo')
# plt.show()

# subplot()

# first data is not showing in bargraph ---- error-----

# name = ['rohit', 'virat', 'pant']
# runs = ['90', '50', '80']
#
# plt.figure(figsize=(9, 3))
#
# plt.subplot(121)
# plt.bar(name, runs)
#
# plt.subplot(122)
# plt.scatter(name, runs)
#
# plt.show()


# Line graph

# fig = plt.figure()
# ax = plt.axes()
#
# waves = np.linspace(0, 10, 100)
# ax.plot(waves, np.sin(waves))
# plt.show()


# Bar Graph

# player = ['Rohit', 'Dhawan', 'Virat', 'Dhoni']
# runs = [60, 80, 99, 54]
# # plt.bar(player, runs)
# plt.barh(player, runs)
# plt.show()


# Pie-Chart
# player = ['Rohit', 'Dhawan', 'Virat', 'Dhoni']
# runs = [60, 80, 99, 54]
#
# explode = (0.1, 0, 0, 0)
#
# fig, ax = plt.subplots()
# ax.pie(runs, explode=explode, labels=player, autopct = '%1.1f%%', shadow=True)
#
# plt.show()



# Histogram

# ages = [51, 71,24, 64, 25, 95, 77, 44, 55, 67, 72, 65]
# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# 
# plt.hist(ages, bins, histtype='bar', rwidth=0.8)
# plt.show()


# Scatter

# x = [5, 7, 10]
# y = [18, 10, 6]
#
# x2 = [6, 9, 11]
# y2 = [7,  14, 17]
#
# plt.scatter(x, y)
#
# plt.scatter(x2, y2, color='g')
# plt.show()


fig = plt.figure()

ax = plt.axes(projection='3d')

weight = np.array([100, 120, 145, 96, 55, 110, 108, 102, 134, 88, 77, 68, 109])
height = np.array([108, 102, 134, 88, 77, 68, 109, 100, 120, 145, 96, 55, 110])

ax.scatter3D(height, weight)
plt.xlabel('weight')
plt.ylabel('height')

plt.show()








