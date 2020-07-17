import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4]
y = [0,2,4,6,8]

plt.plot(x, y, label='2x', color='#37be1c', linewidth=3, marker='.',
        linestyle='--', markersize='10', markeredgecolor='blue'
    )
# use shorthand notation
# fmt = '[color][marker][line]'
# plt.plot(x, y, 'g.--', label='2x')

plt.title('A simple graph', fontdict={'fontname':'Noto Mono', 'fontsize':20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Define values for axes
plt.xticks([0,2,4])
plt.yticks([0,5,10])

plt.legend()

plt.show()
