import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Line graph

gas = pd.read_csv('data/gas_prices.csv')
print(gas)

plt.title('Gas prices over time (in USD)')
plt.plot(gas.Year, gas.USA, label='EEUU')
plt.plot(gas.Year, gas.Mexico, 'g.-', label='Mexico')
plt.plot(gas['Year'], gas['South Korea'], label='South Korea')

# if in plot don't set labels, legend, still, it will works
plt.legend()
plt.xticks(gas.Year[::3]) # every three years
plt.show()
