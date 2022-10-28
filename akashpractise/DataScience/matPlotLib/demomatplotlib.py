from matplotlib import pyplot as plt
from matplotlib import style
from mpl_toolkits import mplot3d
import numpy as np

# basic plotting
# data =plt.plot([1,5,7],[2,8,4])
# print(data)
# plt.show()

# styling

# x= [2,4,5,6]
# y = [3,6,9,10]
# data = plt.plot(x,y,"d")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.title("Basic Graph")
# print(data)
# plt.show()

# name=["Rohit","Romil","Rakesh","Rajesh"]
# marks = [60,50,75,90]
# plt.figure(figsize=(12,4))
# plt.subplot(131)
# plt.barh(name,marks)
# plt.subplot(132)
# plt.bar(name,marks)
# print(data)
plt.show()

# line graph
# fig = plt.figure()
# ax = plt.axes()
# waves = np.linspace(0,10,10)
# ax.plot(waves,np.tan(waves))
# plt.show()

# bar graph
# question?? subplot not work here
# student = ["Akash","Virat","Mohan","Govind"]
# marks = [60,85,96,82]
# plt.figure(figsize=(10, 10))
# plt.subplots(131)
# plt.bar(student,marks)
# plt.subplots(132)
# plt.barh(student,marks)
# plt.show()