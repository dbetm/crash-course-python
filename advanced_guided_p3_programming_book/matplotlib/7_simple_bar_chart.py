import matplotlib.pyplot as plt

# Set up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
colors = ('blue', 'gray', 'black', 'red', 'purple')
sizes = [45, 10, 15, 30, 22]
index = (1, 2, 3, 4, 5) # provides locations on x axis

# Set up the bar chart
plt.bar(index, sizes, tick_label=labels, color=colors)

# Configure the layout
plt.ylabel('Usage')
plt.xlabel('Programming languages')

# Display the chart
plt.show()
