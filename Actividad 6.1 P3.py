# GRAFICAR EXCEL

import pandas as pd
import matplotlib.pyplot as plt

width = 0.25
workbook = "Puntajes.xlsx"
df = pd.read_excel(workbook)
print(df.head())

datos = df[["Nombre", "Álgebra", "Química"]]

#datos.plot.bar(x="Nombre", y="Álgebra", color="green", width=width, rot=0)
datos.plot(x="Nombre", kind="bar", rot=0)
plt.title("Gráfico Excel")
plt.xlabel("Nombres")
plt.ylabel("Puntajes")
plt.grid()
plt.show()
