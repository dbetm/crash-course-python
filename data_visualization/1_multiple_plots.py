# Import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

""" Graficar varias series de datos en una misma gráfica.
"""

# Retry data
data = pd.read_csv('data/enrollment_of_women.csv')
year = np.array(list(data['year']))
physical_sciences = np.array(list(data['physical_science']))
computer_science = np.array(list(data['computer_science']))

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='green')

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')

# Display the plot
plt.show()
