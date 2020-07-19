import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('data/fifa_data.csv')

# Set style of plot
plt.style.use('default')

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']

labels = ['Barcelona', 'Real Madrid']

boxes = plt.boxplot(
        [barcelona, madrid],
        labels=labels,
        patch_artist=True,
        medianprops={'linewidth':2}
    )

colors = ('#468e19', '#911198')
i = 0
for box in boxes['boxes']:
    # Set edge color
    box.set(color=colors[i])
    i += 1
    # Change fill color
    box.set(facecolor='#e0e0e0')

plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA overall rating')

plt.show()
