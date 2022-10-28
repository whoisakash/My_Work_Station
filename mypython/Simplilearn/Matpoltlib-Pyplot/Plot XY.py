import matplotlib.pyplot as plt
from matplotlib import style

# website traffic data
# number of user/visitors on the web site
web_customers = [123, 645, 950, 1290, 1630, 1450, 1034, 1295, 465, 205, 80]
# Time distribution(hourly)
time_hrs = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# select the type of plot
style.use("ggplot")
plt.title("Web site traffic")
# plt.plot(time_hrs, web_customers, color="b", linestyle= "--", linewidth= 2.5)
plt.plot(time_hrs, web_customers,"b", label="WEB TRAFFIC", linewidth= 2.5)
plt.axis([6.5, 17.5, 50, 2000])
plt.xlabel("Hrs")
plt.ylabel("Number of users")
plt.legend()
plt.show()