import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
Salaries = pd.read_csv("Salaries.csv")

# Ver las primeras filas de los datos
print(Salaries.head())

# Verificar duplicados en una columna específica, por ejemplo, 'salary'
print(Salaries.duplicated().any())

# Verificar si hay filas con datos faltantes en cualquier columna
print(Salaries.isnull().values.any())

# Suponiendo que tu conjunto de datos se llama "data" y la columna de rangos académicos se llama "rank"
unique_ranks = Salaries['rank'].unique()
num_unique_ranks = len(unique_ranks)
print(num_unique_ranks, unique_ranks)

# Análisis descriptivo
print(Salaries.describe())

# Convertir la variable "sex" a un formato numérico (variable dumi)
Salaries['sex_numeric'] = np.where(Salaries['sex'] == 'Male', 0, 1)

# Comparación de salarios por género y rango académico
plt.figure(figsize=(10, 6))
sns.boxplot(x='rank', y='salary', hue='sex', data=Salaries)
plt.title('Distribución de salarios por rango académico y género')
plt.xlabel('Rango Académico')
plt.ylabel('Salario')
plt.show()

# Correlación entre género (convertido a numérico) y salario
correlation_matrix = Salaries[['salary', 'sex_numeric']].corr(method='spearman')
print(correlation_matrix)

# Gráfico de dispersión de salario vs. años de servicio
plt.figure(figsize=(10, 6))
plt.scatter(Salaries['yrs.service'], Salaries['salary'])
plt.title('Relación entre años de servicio y salario')
plt.xlabel('Años de Servicio')
plt.ylabel('Salario')
plt.show()
