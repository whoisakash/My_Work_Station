import matplotlib.pyplot as plt

# job data in percentile
# job_data = [40, 20, 17, 8, 5, 10]
# job_data.sort()
job_data = ["40", "20", "17", "8", "5", "10"]
labels = "IT", "Finance", "Marketing", "Admin", "HR", "Operations"

# explode the 1st slice which is IT
explode = (0.05, 0, 0, 0, 0, 0)

plt.pie(job_data, labels= labels, explode= explode)

plt.show()