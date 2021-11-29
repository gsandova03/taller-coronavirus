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

# 7. Ordenar de mayor a menor por tipo de caso (Importado, en estudio, relacionado)
print('--------------------------------tipo de caso ordenado:')
print(data.groupby('Tipo de contagio').size().sort_values(ascending=False))

# 8. Numero de departamentos afectados
print('---------------------departamentos afectados: ')
print(data['Nombre departamento'].unique().size)

# 9. Liste los departamentos afectados sin repetirlos
print('------------------------departamentos afectados sin repetir:')
print(data['Nombre departamento'].unique())

# 10. Ordene de mayor a menor por tipo de atencion
print('-------------------------------tipos de atencion ordenado:')
print(data.groupby('Ubicación del caso').size().sort_values(ascending=False))

# 11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados
print('----------------------------departamento con mas casos de contagio: ')
print(data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10))

# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
print('--------------------------departamento con mas fallecidos:')
print(data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10))

# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados
print('---------------------departamento con mas recuperados: ')
print(data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10))

# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados
print('---------------------------municipios con mas casos de contagio:')
print(data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10))

# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
print('----------------------------municipios con mas casos de fallecidos:')
print(data[data['Recuperado'] == 'fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10))

# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados
print('----------------------------------municipios con mas recuperados: ')
print(data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10))

# 17. Liste agrupado por departamento y en orden de mayor a menor las ciudades con mas casos de contagiados
print('----------------------departamentos con mas casos de contagios:')
print(data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values(ascending=False))

# 18.  Numero de mujeres y hombres contagiados por ciudad por departamento
print('-----------------------hombres y mujeres contagiados por ciudad: ')
print(data.groupby(['Nombre departamento', 'Nombre municipio','Sexo']).size().sort_values(ascending=False))

# 19. Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
print('---------------------------------promedio de edad de contagios: ')
print(data.groupby(['Nombre departamento','Nombre municipio', 'Sexo']).Edad.mean())

# 20. Liste de mayor a menor el numero de contagiados por pais de procedencia
print('----------------------------------numero de contagios por pais: ')
print(data.groupby('Nombre del país').size().sort_values(ascending=False))

# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios
print('-------------------------------fechas con mas contagios: ')
print(data.groupby('Fecha de diagnóstico').size().sort_values(ascending=False))

# 22. Diga cual es la tasa de mortalidad y recuperacion que tiene toda colombia
print('----------------tasa de mortalidad y recuperacion')
# Tasa mortalidad
print(((len(data[data['Recuperado'] == 'fallecido'])) * 100) / (len(data)))
# Tasa de recuperados
print(((len(data[data['Recuperado'] == 'Recuperado'])) * 100) / (len(data)))

# 23. Liste la tasa de mortalidad y recupercaion que tiene cada departamento# Mortalidad
print('-------------tasa de mortalidad y recuperacion por departamento: ')
print((data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size() / len(data)) * 100)
# Recuperacion
print((data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size() / len(data)) * 100)

#27  Grafique las curvas de contagio, muerte y recuperación de toda Colombia acumulados
#contagiados
data.groupby('Fecha de diagnóstico').size().sort_values().plot()
#Fallecidos
data[data['Recuperado'] == 'fallecido'].groupby('Fecha de diagnóstico').size().sort_values().plot()
#Recuperados
data[data['Recuperado'] == 'Recuperado'].groupby('Fecha de diagnóstico').size().sort_values().plot()