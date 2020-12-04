import matplotlib.pyplot as plt
import numpy as np

# Set up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5) # provides locations on x axis
web_usage = [20, 2, 5, 10, 14]
data_science_usage = [15, 8, 5, 15, 2]
games_usage = [10, 1, 5, 5, 4]

# Set up the bar chart
plt.bar(index, web_usage, tick_label=labels, label='web')
plt.bar(index, data_science_usage, tick_label=labels, label='data science', bottom=web_usage)

web_plus_data_science = list(np.array(web_usage) + np.array(data_science_usage))
plt.bar(index, games_usage, tick_label=labels, label='games', bottom=web_plus_data_science)

# Configure the layout
plt.ylabel('Usage')
plt.xlabel('Programming languages')
plt.legend()

# Display the chart
plt.show()
