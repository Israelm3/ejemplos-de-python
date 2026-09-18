import pandas as pd
import matplotlib.pyplot as plt
import math
import mysql.connector
import numpy as np
from mysql.connector import Error  # Corrección aquí
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pandas")


# Configuración de conexión MySQL
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ecbd'
}

try:
    # Establecer conexión
    conexion = mysql.connector.connect(**config)

    if conexion.is_connected():
        print("Conexión exitosa a MySQL")

        # Consulta SQL
        query = """
        SELECT
            v.venta_id AS VentaID,
            s.codigo AS Sucursal,
            ve.nombre_completo AS Vendedor,
            v.precio AS Precio,
            v.contidad AS Cantidad
        FROM venta v
        JOIN sucursales s ON v.sucursal_id = s.sucursal_id
        JOIN vendedores ve ON v.vendedor_id = ve.vendedor_id
        """

        # Leer datos en un DataFrame
        datos = pd.read_sql(query, conexion)

        print("\n Columnas:", datos.columns.tolist())
        print(datos.head())
        print(datos.info())

        # Limpieza de 'Sucursal'
        if 'Sucursal' in datos.columns:
            datos['Sucursal'] = datos['Sucursal'].replace({
                'Nte': 'Norte',
                'Cte': 'Centro',
                'Sur': 'Sur'
            })
            print("\n Valores únicos en Sucursal:", datos['Sucursal'].unique())
        else:
            print("\n Error: No se encontró la columna 'Sucursal'")
            print("Columnas disponibles:", datos.columns.tolist())
            exit()

        # Configuración de estilo
        plt.style.use('seaborn-v0_8')
        plt.rcParams['figure.figsize'] = (10, 6)

        # 1. Gráfico de pastel: ventas por sucursal
        plt.figure()
        datos['Sucursal'].value_counts().plot(
            kind='pie',
            autopct='%1.1f%%',
            startangle=90,
            colors=['#ff9999', '#66b3ff', '#99ff99'],
            explode=(0.05, 0.05, 0.05)
        )
        plt.title('Distribución de Ventas por Sucursal')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig('Ventas_por_Sucursal.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 2. Gráfico de barras: ventas por vendedor
        plt.figure()
        ventas_por_vendedor = datos['Vendedor'].value_counts().sort_values()
        ventas_por_vendedor.plot(kind='barh', color='#1177b4', edgecolor='black')
        plt.title('Ventas por Vendedor')
        plt.xlabel('Número de Ventas')
        plt.ylabel('Vendedor')
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('Ventas_por_Vendedor.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 3. Gráfico de dispersión: Precio vs. Cantidad
        plt.figure()
        plt.scatter(datos['Precio'], datos['Cantidad'], alpha=0.6, color='green',
                    edgecolors='black', linewidths=0.5)
        plt.title('Relación entre Precio y Cantidad Vendida')
        plt.xlabel('Precio (USD)')
        plt.ylabel('Cantidad Vendida')
        plt.grid(True, linestyle='--', alpha=0.5)

        # Línea de tendencia
        z = np.polyfit(datos['Precio'], datos['Cantidad'], 1)
        p = np.poly1d(z)
        plt.plot(datos['Precio'], p(datos['Precio']), "r--")
        plt.tight_layout()
        plt.savefig('Precio_vs_Cantidad.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 4. Histograma: Distribución de Precios
        plt.figure()
        n_bins = int(1 + 3.3 * math.log10(len(datos)))
        plt.hist(datos['Precio'], bins=n_bins, color='#ff7f0e', edgecolor='black', alpha=0.7)
        plt.title('Distribución de Precios de Ventas')
        plt.xlabel('Precio (USD)')
        plt.ylabel('Frecuencia')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('Distribucion_Precios.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("\n ¡Análisis completado y gráficos generados!")

except Error as e:
    print(f"\n Error en la conexión a MySQL: {e}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("\n Conexión a MySQL cerrada correctamente.")
