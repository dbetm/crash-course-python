import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('data/fifa_data.csv')

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

colors = ['#0dc869', '#cc4317']
labels = ['Left foot', 'Right foot']
plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')
plt.title('Foot preference of FIFA players')

plt.show()
