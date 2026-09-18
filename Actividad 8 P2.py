import pandas as pd
import matplotlib.pyplot as plt
import math

# Datos para el archivo CSV
datos = {
    'ventaID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'sucursal': ['Nte', 'Cte', 'Sur', 'Nte', 'Cte', 'Sur', 'Cte', 'Nte', 'Sur', 'Cte'],
    'vendedor': ['Juan', 'Ana', 'Luis', 'Ana', 'Juan', 'Luis', 'Ana', 'Luis', 'Juan', 'Ana'],
    'precio': [100, 150, 120, 130, 90, 200, 80, 110, 170, 160],
    'cantidad': [5, 3, 4, 2, 6, 1, 7, 3, 2, 4]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Guardar como CSV
df.to_csv('ventas.csv', sep=';', index=False, encoding='latin1')

# Cargar el archivo CSV
datos = pd.read_csv('ventas.csv', sep=';', encoding='latin1')

# Normalizar columnas a minúsculas
datos.columns = datos.columns.str.strip().str.lower()

# Limpieza de la columna 'sucursal'
datos['sucursal'] = datos['sucursal'].replace({'nte': 'Norte', 'cte': 'Centro', 'sur': 'Sur'})

# Gráfico de pastel: ventas por sucursal
plt.figure()
datos.groupby('sucursal').count()['ventaid'].plot(kind='pie', autopct='%1.1f%%')
plt.title('Ventas por sucursal')
plt.ylabel('')
plt.savefig('ventas_por_sucursal.pdf')

# Gráfico de barras: ventas por vendedor
plt.figure()
datos.groupby('vendedor').count()['ventaid'].plot(kind='bar')
plt.xlabel('Vendedor')
plt.ylabel('Cantidad de ventas')
plt.title('Ventas por vendedor')
plt.savefig('ventas_por_vendedor.pdf')

# Gráfico de dispersión: precio vs. cantidad vendida
plt.figure()
datos.plot.scatter(x='precio', y='cantidad')
plt.title('Precio vs cantidad vendida')
plt.xlabel('Precio')
plt.ylabel('Cantidad')
plt.savefig('precio_vs_cantidad.pdf')

# Histograma de precios
plt.figure()
rango = datos['precio'].max() - datos['precio'].min()
intervalos = 1 + 3.3 * math.log10(len(datos))
amplitud = max(1, round(rango / round(intervalos)))
plt.hist(datos['precio'], bins=amplitud, color='blue')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.title('Histograma de precios')
plt.grid(True)
plt.savefig('histograma_precios.pdf')

print("Se creó el archivo 'ventas.csv' y los gráficos PDF.")
