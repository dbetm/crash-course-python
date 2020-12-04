import numpy as np
import matplotlib.pyplot as plt

x = (5, 5.5, 6, 6.5, 7, 8, 9, 10)
y = (120, 115, 100, 112, 80, 85, 69, 65)

# Generate the scatter plot
plt.scatter(x, y)

# Generate trend line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), 'r')

# Display the figure
plt.show()
