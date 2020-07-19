import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('data/fifa_data.csv')

# Select weights column (and do data cleaning)
fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]
# Set style of plot
plt.style.use('seaborn-dark')

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa.loc[fifa.Weight >= 200].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['< 125', '[125,150)', '[150, 175)', '[175,200)', '>= 200']

# Separation of center mass
explode = (.0, .2, .0, .2, .2)
plt.title('Weight distribution of FIFA players (lbs)')
plt.pie(weights, labels=labels, autopct="%.2f %%", pctdistance=0.7, explode=explode)

plt.show()
