import matplotlib.pyplot as plt
import numpy as np

# student = [40,55,100,80,25]
# gread= ["A","B","C","D","E"]
# exp=[0,0,0.2,0,0]
# clr=['red','blue','yellow','brown','green']
# plt.title("Student Gread Rate")
# plt.pie(student, labels=gread, explode=exp, autopct='%2.1f%%', colors=clr)
# plt.show()

# x=[0,5,10,15,20,25,30]
# y1=[10,15,20,20,30,15,0]
# y2=[10,12,15,12,20,10,0]
# plt.plot(x,y1,linestyle="dashed",marker="+",label="line-1")
# plt.plot(x,y2,linestyle="dashed",marker="o",label="line-2")
# plt.title("Velocity-Time Graph")
# plt.xlabel("Velocity m/s")
# plt.ylabel("Time(s)")
# plt.legend()
# plt.show()

# x=np.arange(1,11,1)
# y1=(2*x)+1
# y2=(2*x*x)+2
# plt.plot(x,y1,"g",linewidth=3,label="y=2x+1")
# plt.plot(x,y2,"r",linewidth=3,label="y=2x^2+2")
# plt.legend()
# plt.show()


from mpl_toolkits import mplot3d

# fig = plt.figure()
#
# ax = plt.axes(projection='3d')
#
# runs = np.array([100, 110, 65, 85, 95, 45, 75])
# years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021])
#
# ax.scatter3D(runs, years)
# plt.show()
'''bar chart'''
state = ["Panjab","Haryana","U.P","M.P","Kerala","Rajasthan"]
area = [220,120,100,40,80,30]
plt.bar(state,area,color= "green",edgecolor="yellow")
plt.xlabel("State")
plt.ylabel("Area(Lac hectares")
plt.title("Wheat Cultivation")
plt.show()

# '''multibar chart'''
# # import matplotlib.pylot as plt
# # import numpy as np
# x=["a","b","c","d"]
# Score=[[5,25,45,20],[4,23,49,17],[6,22,47,19]]
# x= np.arange(4)
# plt.bar(x+0.00,Score[0],color="r",width=[0.25])
# plt.bar(x+0.25,Score[1],color="g",width=[0.25])
# plt.bar(x+0.5,Score[2],color="b",width=[0.25])
# plt.xticks(x,["a","b","c","d"])
# plt.show()