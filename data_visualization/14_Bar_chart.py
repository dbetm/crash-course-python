import matplotlib.pyplot as plt
import numpy as np

labels = ['A', 'B', 'C']
values = [1, 4, 2]

bars = plt.bar(labels, values, color='green')

patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.show()
