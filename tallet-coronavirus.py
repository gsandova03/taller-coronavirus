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

# 1. Numero de casos en el pais
print('---------------numero de casos:')
print(data['ID de caso'].count())

# 2. Numero de municipios afectados
print('---------------numero de municipios:')
print(data['Nombre municipio'].unique().size)

# 3. Liste los municipios afectados (sin repetirlos)
print('---------------municipios afectados:')
print(data['Nombre municipio'].unique())

# 4. Numero de personas que se encuentran en atencion en casa
print('--------------------numero de personas atencion en casa:')
print(len(data[data['Ubicación del caso'] == 'casa']))

# 5. Numero de personas que se encuentran recuperados
print('-------------------numero de personas recuperadas:')
print(len(data[data['Recuperado'] == 'Recuperado']))

# 6. Numero de personas que han fallecido
print('-------------------numero de personas fallecidas:')
print(len(data[data['Recuperado'] == 'fallecido']))