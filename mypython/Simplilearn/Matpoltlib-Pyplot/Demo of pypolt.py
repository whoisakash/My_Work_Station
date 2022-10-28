'''Problem Statement
You have been provided with a dataset that lists Ohio State's leading causes of death from
the year 2012.
Using the two data points cause of death and percentile, draw a pie chart to visualize the
dataset.'''

import matplotlib.pyplot as plt

'''Data from ohio state, Leading causes of death in the state from year 2012
cause of deaths'''

cause = "Chronic Diseases", "Unintentional Injuries", "Alzheimers", "Infuenza and Pneumonia", "Sepsis", "Others"

# PERCENTILE
percentile = [62, 5, 4, 2, 1, 26]

# set the pie chart plot properties
# set figure size
plt. figure(figsize= (10, 10))

# explode the largest pie in the data set
expload = (0.05, 0, 0, 0, 0, 0)

# set pie chart properties
plt.pie(percentile, labels=cause, explode=expload, autopct="%1.1f%%", startangle=70)

# set axis equal to draw pir as circle
plt.axis("equal")

# set title of the pie chart
plt.title("Ohio State-2012 Leading Causes of Death")

plt.show()


