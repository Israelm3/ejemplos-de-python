# El código tiene como objetivo graficar y comparar las funciones trigonométricas 
# básicas (seno, coseno y tangente) en un rango de 
# -2p a 2p, permitiendo:

# * Identificar patrones (periodicidad, amplitud, asíntotas).
# * Entender diferencias clave entre las funciones.
# * Visualizar conceptos matemáticos como: ceros, máximos/mínimos.
# * Puntos notables (π/2, π, etc.).
# * Comportamiento de la tangente (discontinuidades).

import matplotlib.pyplot as plt
import numpy as np

# funciones
fn_1 = np.sin
fn_2 = np.cos
fn_3 = np.tan

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
points = [i * np.pi / 2 for i in range(-4, 5)]
labels = ["-2p", "-3p/2", "-p", "-p/2", "0", "p/2", "p", "3p/2", "2p"]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x, fn_1(x), label="seno")
ax.plot(x, fn_2(x), label="coseno")
ax.plot(x, fn_3(x), label="tangente")

ax.set_xticks(points)
ax.set_xticklabels(labels)

plt.ylim(-5, 5)
ax.hlines(0, -7, 7, "black")
ax.vlines(0, -5, 5, "black")

plt.title("Gráficas Trigonométricas")
plt.grid()
plt.legend()
plt.show()
