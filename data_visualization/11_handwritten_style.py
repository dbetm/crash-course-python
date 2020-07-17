import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3]
y = [1,2,3]

with plt.xkcd():
    plt.title("Simple graph",
        fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.plot(x, y)
    plt.show()
