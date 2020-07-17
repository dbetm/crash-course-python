import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4]
y = [0,2,3,6,8]
# Line number 1
plt.plot(x, y, 'b^-', label='2x')
#Line number 2

x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:4], x2[:4]**2, 'r', label='x^2')
plt.plot(x2[3:], x2[3:]**2, 'r--')

plt.title('A simple graph', fontdict={'fontname':'Noto Mono', 'fontsize':20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()
