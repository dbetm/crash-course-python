import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('data/fifa_data.csv')
print(fifa.head(5))
print(len(fifa))

bins = [30,40,50,60,70,80,90,100]

plt.hist(fifa.Overall, bins=bins)
plt.ylabel('Num players')
plt.xlabel('Skill level')
plt.title('Distribution of player skills in FIFA 2018')

plt.xticks(bins)
plt.show()
