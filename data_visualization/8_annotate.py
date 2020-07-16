import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""It is often useful to annotate a simple plot to provide context. This makes
the plot more readable and can highlight specific aspects of the data.
Annotations like text and arrows can be used to emphasize specific observations.
"""

# Retry data
data = pd.read_csv('data/enrollment_of_women.csv')
year = np.array(list(data['year']))
physical_sciences = np.array(list(data['physical_science']))
computer_science = np.array(list(data['computer_science']))

# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Plot the % of degrees awarded to women in Computer Science and the Physical Sciences
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.plot(year, computer_science, color='red', label='Computer Science')

plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')

# Add a legend at the lower center
plt.legend(loc='lower right')

# Add a black arrow annotation
plt.annotate(
    'Maximum', xy=(yr_max, cs_max),
    xytext=(yr_max+5, cs_max+5), arrowprops=dict(facecolor='black')
    )

plt.title('Undergraduate enrollment of women')

plt.show()
