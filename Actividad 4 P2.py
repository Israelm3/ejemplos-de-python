import pandas as pd
import matplotlib.pyplot as plt

# Crear datos desde cero
datos = {
    'materia': ['Algebra', 'Algebra', 'Algebra', 'Quimica', 'Quimica', 'Quimica'],
    'tiempo': [1, 2, 3, 1, 2, 3],
    'nota': [5, 7, 9, 6, 6.5, 8]
}

# Crear y guardar archivo CSV
df = pd.DataFrame(datos)
df.to_csv("dispersion.csv", index=False)
print("Archivo 'dispersion.csv' creado exitosamente.")

#Leer archivo CSV
df = pd.read_csv("dispersion.csv")

#filtrar los datos por materia
algebra_data = df[df['materia'] == 'Algebra']
quimica_data = df[df['materia'] == 'Quimica']

#Extraer las columnas de tiempo y notas
tiempo_algebra = algebra_data['tiempo']
notas_algebra = algebra_data['nota']

tiempo_quimica = quimica_data['tiempo']
notas_quimica = quimica_data['nota']

#Caracteristicas del grafico
plt.scatter(tiempo_algebra, notas_algebra, color="black", label="Algebra")
plt.scatter(tiempo_quimica, notas_quimica, color="red", label="Quimica")

#Titulo y etiquetas
plt.title("Diagrama de dispersion")
plt.xlabel("Horas de estudio")
plt.ylabel("Notas de estudio")

#Mostrar leyenda y grafico
plt.legend(loc="upper left")
plt.grid()
plt.savefig("diagrama_dispersion.png")
plt.show()


#Interpretacion de grafico
#Posible correlacion positiva: Si los puntos tienden a subir hacia la derecha,
#Sugiere que a mas horas de estudio, mejores notas,

#Diferencias entre asignaturas: Permite comparar si una materia requiere mas
#tiempo para lograr notas similares

#Outliers: Puntos alejados de la tendencia (ej: en Quimica, 9 horas ? nota 11)
#podrian indicar otros factores influyentes.
