#la empresa Rinco Matic S.A. de C.V, se dedica a la fabricacion de muebles escolares, asi como muebles de
#cocina, es una empresa reconocida por la calidad que ofrece en sus productos,sin embargo en este ultimo mes
#de abril del presente año ha recibido quejas por parte de sus clientes que adquieren muebles como pupitres
#escolares, puesto que la cubierta de terciado de las paletas para los mesa-bancos se desprendiancon
#facilitar. es por ello que la empresa ha reaccionado de la manera mas rapida posible, encomendado al
#jefe de produccion le justifique el por que de esos defectos mencionados, a grandes rasgos el jefe de
#produccion menciono que se tenia problemas en el area de elaboracion de las paletas para los mesa-bancos,
#por lo que la empresa pidio respaldo de lo mencionado y tomara cartas en el asunto y desde luego brindara
#una respuesta inmediata.
#por lo que el jefe de produccion primeramente  ha de determinar el tamaño de muestra de analizar tomada de un
#lote de produccion identificando el problema en el grosor de la cubierta de terciado por lo que el sellador
#que se coloca para la misma no es suficiente y por ende en el area de desamble de la mesa-bancos se tenian
#dificultades a la hora de fijar con las pijas.
#los datoa obtenidos fueron los siguientes:
#
#17.89 17.91 17.03 17.03 17.97 17.97 18.01 18.01 18.03 18.05 18.08 18.11 18.12 18.12 18.14 18.14 18.16 18.16
#18.17 18.18 18.19 18.21 18.22 18.22 18.32
#
#comprobar que los datos tengan un comportamiento normal, por medio de una prueba


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

#datos proporcionados
datos = np.array([
    17.89, 17.91, 17.03, 17.03, 17.97, 17.97, 18.01, 18.01, 18.03, 18.05, 18.08,
    18.11, 18.12, 18.12, 18.14, 18.14, 18.16, 18.16, 18.17, 18.18, 18.19, 18.21,
    18.22, 18.22, 18.32])

#1- prueba de normalidad (shapiro-wilk)
shapiro_test = stats.shapiro(datos)
print("--- Prueba de normalidad (shapiro-wilk)---")
print(f"estadistico w: {shapiro_test.statistic:.4f}")
print (f"valor o: {shapiro_test.pvalue:.4f}")
if  shapiro_test.pvalue > 0.05:
    print("conclusion: los datos siguen una distribucion normal (p > 0.05).")
else:
        print("conclusion: los datos NO siguen una distancia normal (p = 0.05). ")

#2- medidas de tendencia central
        media = np.mean(datos)
        mediana = np.median(datos)
        moda = stats.mode(datos, keepdims=True).mode[0]

print("\n--- medidas de tendencia central ---")
print(f"media: {media:.4f} mm")
print(f"mediana: {mediana: .4f} mm")
print(f"moda: {moda:.4f} mm")

#3. Medidas de dispersion
desviacion_std = np.std(datos, ddof=1) # ddof=1 para muestra (no poblacion)
varianza = np.var(datos, ddof=1)
rango = np.max(datos) - np.min(datos)
rango_intercuartil = stats.iqr(datos)

print ("\n--- Medidas de dispersion ---")
print(f"desviacion estandar: {desviacion_std:.4f} mm")
print(f"varianza: {varianza:.4f} mm²")
print(f"rango: {rango:.4f} mm")
print(f"rango intercuartil (IQR): {rango_intercuartil:.4f} mm")

#4 visualizacion
plt.figure(figsize=(12, 15))

#histograma + curva de densidad
plt.subplot(1, 2, 1)
sns.histplot(datos, kde=True, color='blue', bins=6)
plt.title('distribucion del grosor de terciado')
plt.xlabel('grafico (mm)')
plt.ylabel('frecuencia')

#grafico Q-Q
plt.subplot(1, 2, 2)
stats.probplot(datos, plot=plt)
plt.title('grafico Q-Q para normalidad')

plt.tight_layout()
plt.show()

#interpretacion adicional
print("\n--- interpretacion de resultados ---")
if shapiro_test.pvalue > 0.05:
    print("- los datos son normales, por lo que las tecnicas parametricas son validas.")
else:
        print("- los datos NO son normales, considere pruebas no parametricas.")

print(f"- la medida del grosor es {media:.2f} mm. Si el estandar de diseño es mayor, hay problemas de adhesion.")
print(f"- la desviacion estandar de {desviacion_std:.2f} mm indica variabilidad en el proceso.")
print(f"- valores atipicos potenciales: 17.03 mm (revisar causa).")
