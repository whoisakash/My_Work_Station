import matplotlib.pyplot as plt

cause = "Chronic Diseases", "Unintentional Injuries", "Alzheimers", "Infuenza and Pneumonia", "Sepsis", "Others"

# PERCENTILE
percentile = [62, 5, 4, 2, 1, 26]

# set the pie chart plot properties

plt.figure(figsize=(10,10))
explode=(0.05, 0, 0, 0, 0, 0)
plt.pie(percentile, labels=cause, explode=explode,autopct="%1.1f%%", startangle=70)
# set axis equal to draw pie as circle
plt.axis("equal")
plt.title("Ohio State - 2012 : Leading Causes of Death")
plt.show()