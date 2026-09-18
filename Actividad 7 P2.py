#en una ciudad, la contaminacion del aire (CO2) y el trafico vehicular estan
#relacionados, Supongamos que:
#la funcion cuadratica ( f(x)=x**2) respeta el aumentono lineal de la contaminacion a medida que crece
#el numero de vehiculo (x).
#a mayor trafico, la contaminacion aumenta aceleradamente
#(por congestion, mala combustion, etc).
#la funcion lineal (f(x)=4x+5) modela el crecimineto lineal de la infraestructura vial
#capacidad de vias o semaforos)
#cada nuevo carril o semaforo reduce practicamente el problema,
#pero no lo resuelve exponencialmente.

#objetivo:
#encontrar el punto de equilibrio (interseccion) dodne la contaminacion y
#la estructura se igualan, para determinar politicas efectivas
#(ej. limite de vehiculos o inversion de trasporte publico).


import matplotlib.pyplot as plt
import numpy as np

# Función 1: contaminación (crecimiento cuántico por tráfico)
def contaminacion(x):
    return x**2

# Función 2: infraestructura vial (crecimiento lineal)
def infraestructura(x):
    return 4*x + 5

# Rango de vehículos (en miles)
x = range(0, 15)

# Graficar funciones
plt.plot(x, [contaminacion(i) for i in x], color="red", label="Contaminación (CO2) = x²")
plt.plot(x, [infraestructura(i) for i in x], color="blue", label="Infraestructura = 4x + 5")

# Ejes y título
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Impacto del tráfico en la contaminación y la infraestructura")
plt.xlabel("Número de vehículos (miles)")
plt.ylabel("Nivel de impacto")
plt.grid(linestyle="--", alpha=0.6)
plt.legend()

# Punto de equilibrio (intersección)
# Resolver: x² = 4x + 5 -> x² - 4x - 5 = 0
soluciones = np.roots([1, -4, -5])
x_sol = [sol for sol in soluciones if sol >= 0][0]  # Tomar solución positiva
y_sol = contaminacion(x_sol)

# Dibujar punto de equilibrio
plt.scatter(x_sol, y_sol, color="green", zorder=5, label=f"Equilibrio: x ≈ {x_sol:.2f}")
plt.annotate(f'Política óptima: {x_sol:.2f} mil vehículos',
             xy=(x_sol, y_sol),
             xytext=(5, 100),
             arrowprops=dict(arrowstyle="->"))

plt.show()
