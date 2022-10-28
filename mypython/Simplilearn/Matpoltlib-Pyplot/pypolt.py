import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Generate random number
randomNum = np.random.rand(10)
# print(randomNum)

# Select Stylefor the plot
style.use("ggplot")

# plot the random number
plt.plot(randomNum, "g", label=" line one", linewidth=2)

plt.xlabel("Range")
plt.ylabel("Number")

plt.title("First Plot")
plt.legend()
plt.show()