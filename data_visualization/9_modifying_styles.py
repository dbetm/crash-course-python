import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Retry data
data = pd.read_csv('data/enrollment_of_women.csv')
year = np.array(list(data['year']))
physical_sciences = np.array(list(data['physical_science']))
computer_science = np.array(list(data['computer_science']))

education = np.array([74.53532758, 74.14920369, 73.55451996, 73.50181443,
        73.33681143, 72.80185448, 72.16652471, 72.45639481, 73.19282134, 73.82114234,
        74.98103152, 75.84512345, 75.84364914, 75.95060123, 75.86911601,
        75.92343971, 76.14301516, 76.96309168, 77.62766177, 78.11191872,
        78.86685859, 78.99124597, 78.43518191, 77.26731199, 75.81493264,
        75.12525621, 75.03519921, 75.1637013 , 75.48616027, 75.83816206,
        76.69214284, 77.37522931, 78.64424394, 78.54494815, 78.65074774,
        79.06712173, 78.68630551, 78.72141311, 79.19632674, 79.5329087 ,
        79.61862451, 79.43281184]
    )

health = np.array([77.1, 75.5, 76.9, 77.4, 77.9, 78.9, 79.2, 80.5, 81.9,
        82.3, 83.5, 84.1, 84.4, 84.6, 85.1, 85.3, 85.7, 85.5, 85.2, 84.6, 83.9, 83.5,
        83. , 82.4, 81.8, 81.5, 81.3, 81.9, 82.1, 83.5, 83.5, 85.1, 85.8,
        86.5, 86.5, 86. , 85.9, 85.4, 85.2, 85.1, 85. , 84.8]
    )

# Set the style to 'dark_background'
plt.style.use('dark_background')
# print all the available style sheets
print(plt.style.available)

# Create a figure with 2x2 subplot layout
plt.subplot(2, 2, 1)

# Plot the enrollment % of women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Plot the enrollment % of women in Computer Science
plt.subplot(2, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Add annotation
cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1, cs_max-10), arrowprops=dict(facecolor='black'))

# Plot the enrollmment % of women in Health professions
plt.subplot(2, 2, 3)
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Plot the enrollment % of women in Education
plt.subplot(2, 2, 4)
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve spacing between subplots and display them
plt.tight_layout()
plt.show()
