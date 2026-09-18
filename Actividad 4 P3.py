#Este código tiene como objetivo visualizar y analizar la distribución de casos 
#de COVID-19 en diferentes regiones del Perú a lo largo de los meses del año 
#2022, utilizando un mapa de calor para identificar patrones geográficos y 
#temporales.

#? Identificar regiones críticas: Detectar qué regiones tuvieron mayor incidencia de contagios.
#? Analizar tendencias temporales: Observar si hubo meses con picos de contagio (ej. olas pandémicas).
#? Comparación regional: Evaluar diferencias en la propagación del virus entre distintas zonas del Perú.
#? Toma de decisiones: Servir como herramienta visual para autoridades sanitarias en la planificación 
#de estrategias de prevención.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("datos_calor.csv", index_col=0)

# Extraen los datos y las etiquetas
data = df.values                 # Matriz de datos
xlabs = df.columns.tolist()     # Nombres de las regiones (columnas)
ylabs = df.index.tolist()       # Nombres de los meses (índice)

# Mapa de calor
fig, ax = plt.subplots()
im = ax.imshow(data, cmap="viridis")   # Usar un mapa de colores

# Agregar las etiquetas
ax.set_xticks(np.arange(len(xlabs)), labels=xlabs)
ax.set_yticks(np.arange(len(ylabs)), labels=ylabs)

# Agregar la leyenda
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("leyenda", rotation=90, va="bottom")

# Agregar los valores a la gráfica
for i in range(len(ylabs)):
    for j in range(len(xlabs)):
        text = ax.text(j, i, round(data[i, j], 1), ha="center", va="center", color="white")

# Rotar las etiquetas del eje X
plt.setp(ax.get_xticklabels(), rotation=40, ha="right", rotation_mode="anchor")

# Título
plt.title("MAPA DE CALOR - CORONAVIRUS (2022)")

# Mostrar la gráfica
plt.tight_layout()
plt.show()
