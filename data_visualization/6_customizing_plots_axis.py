import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""In this exercise, you will work with the matplotlib.pyplot interface to
quickly set the x- and y-limits of your plots using axis.
"""

# Retry data
data = pd.read_csv('data/enrollment_of_women.csv')
year = np.array(list(data['year']))
physical_sciences = np.array(list(data['physical_science']))
computer_science = np.array(list(data['computer_science']))

# Plot the % of degrees awarded to women in Computer Science and the Physical Sciences
plt.plot(year,computer_science, color='red')
plt.plot(year, physical_sciences, color='blue')

plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')

# Set the x-axis and y-axis limits
plt.axis([1990, 2010, 0, 50])

# Save the figure as 'axis_limits.png'
plt.savefig('axis_limits.png')

plt.show()
