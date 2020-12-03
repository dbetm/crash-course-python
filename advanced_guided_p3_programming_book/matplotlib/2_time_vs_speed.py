import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 2, 6, 14, 30, 43, 75]

# Set the axes headings
plt.ylabel('Speed', fontsize=12)
plt.xlabel('Time', fontsize=12)

# Title
plt.title('Time vs Speed')

# Plot and display the graph
plt.plot(x, y, 'b+-')
plt.show()
