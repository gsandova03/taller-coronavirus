import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('covid_22_noviembre.csv')

# data.columns()
data.info()

plt.xticks(rotation=90)

data['Ubicación del caso'].replace('Casa', 'casa', inplace=True)
data['Ubicación del caso'].replace('CASA', 'casa', inplace=True)
data['Recuperado'].replace('Fallecido', 'fallecido', inplace=True)