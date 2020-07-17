from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://www.worldometers.info/world-population/population-by-country/'
table_id = 'example2'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

population_table = soup.find('table', attrs={'id':table_id})
df = pd.read_html(str(population_table))[0]

countries = list(df['Country (or dependency)'])
countries = countries[:20]
num_people = np.array(list(df['Population (2020)']))
num_people = num_people[:20]

plt.bar(countries, num_people)
plt.xticks(rotation='vertical')
plt.ylabel('Num people')
plt.xlabel('Countries')
plt.title('Countries in the world by population (2020)')
plt.tight_layout()
plt.show()
