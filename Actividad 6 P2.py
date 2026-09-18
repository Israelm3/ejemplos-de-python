# --------------------------------------------------------------------------------------
# El objetivo de este código es visualizar múltiples conjuntos de datos relacionados
# con ventas, rendimiento académico y comparativas empresariales en un único cuadro de
# gráficos (dashboard) para facilitar el análisis comparativo y la toma de decisiones.
# Combina cuatro tipos de gráficos en una misma figura, cada uno diseñado para resaltar
# patrones específicos en los datos.
#
# Escenario:
# Un analista de negocios o investigador educativo necesita presentar un informe integral
# que incluya:
# - Tendencias financieras (ventas anuales en dólares).
# - Distribución de productos más vendidos.
# - Rendimiento académico vinculado a horas de estudio.
# - Comparación histórica entre dos empresas.
# --------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

# ------ Plot 1: Ventas anuales en dólares
dolares = [7000, 6500, 7400, 8500]
years = [2019, 2020, 2021, 2022]

plt.subplot(2, 2, 1)  # 2 filas, 2 columnas, posición 1
plt.plot(years, dolares, linewidth=3)
plt.xticks(years)
plt.ylabel("Dólares")
plt.title("Ventas anuales", fontsize=12)

# ------ Plot 2: Distribución de productos más vendidos
productos = ["cuadernos", "lapices", "reglas", "hojas", "folder"]  # 5 productos
cantidad = [5000, 10000, 8000, 3000, 2000]  # Coincide en longitud

plt.subplot(2, 2, 2)  # 2 filas, 2 columnas, posición 2
plt.pie(cantidad, labels=productos, autopct='%1.0f%%')
plt.title("Productos más vendidos", fontsize=12)

# ------ Plot 3: Rendimiento académico vs. horas de estudio
tiempo_algebra = [1, 3, 5, 7]
notas_algebra = [2, 12, 14, 16]

tiempo_quimica = [1, 3, 4, 7]
notas_quimica = [12, 15, 13, 11]

plt.subplot(2, 2, 3)  # 2 filas, 2 columnas, posición 3
plt.scatter(tiempo_algebra, notas_algebra, color="black", label="Álgebra")
plt.scatter(tiempo_quimica, notas_quimica, color="red", label="Química")
plt.title("Diagrama de dispersión", fontsize=12)
plt.xlabel("Horas de estudio")
plt.ylabel("Notas")
plt.legend()

# ------ Plot 4: Comparación histórica entre dos empresas (diagrama de áreas)
sales_a = [2, 3.5, 4.5, 5.2, 3, 7, 5.5]
sales_b = [1, 2.3, 3.1, 4.5, 2, 4.2, 4.3]
years = [2015, 2016, 2018, 2019, 2020, 2021, 2022]

plt.subplot(2, 2, 4)  # 2 filas, 2 columnas, posición 4
plt.fill_between(years, sales_a, label="EMPRESA A", color="green")
plt.fill_between(years, sales_b, label="EMPRESA B", color="blue")
plt.title("Diagrama de áreas", fontsize=12)
plt.legend(loc="upper left")

# ------ Título general del dashboard
plt.suptitle("MÚLTIPLES DIAGRAMAS", fontsize=18)

# Ajustes para que no se sobrepongan los elementos visuales
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# Mostrar todos los gráficos
plt.show()
