import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""Legends are useful for distinguishing between multiple datasets displayed
on common axes. The relevant data are created using specific line colors or
markers in various plot commands. Using the keyword argument label in the
plotting function associates a string to use in a legend.
"""

# Retry data
data = pd.read_csv('data/enrollment_of_women.csv')
year = np.array(list(data['year']))
physical_sciences = np.array(list(data['physical_science']))
computer_science = np.array(list(data['computer_science']))

# Plot the % of degrees awarded to women in Computer Science and the Physical Sciences
plt.plot(year,computer_science, color='red', label='Computer Science')
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')

plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')

# Add a legend at the lower center
plt.legend(loc='lower center')

plt.title('Undergraduate enrollment of women')

plt.show()
