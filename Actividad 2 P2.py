#La empresa DENTASTIX S.A. de C.V, se dedicaba a la fabricación de monedas mexicanas de 20 centavos,  
#es una empresa reconocida por la calidad que ofrecía en sus monedas, sin embargo no sigue haciendo  
#monedas ya que obtenía demasiados errores y la calidad para ella es lo principal, recibió quejas por  
#parte del gobierno.  
#
#Es por ello que la empresa a pesar de ya no fabricar ese tipo de monedas ha reaccionado de la manera  
#más tranquila, dirigiéndose a su jefe de producción para saber el porqué de ese tipo de defectos  
#surgidos, el jefe de producción ha mencionado que se tenía problemas en el área de elaboración  
#(la máquina y el que la trabajaba). Por lo tanto ello originó que la empresa de lo mencionado tomara  
#cartas en el asunto y desde luego su respuesta a su problema fuese inmediata.  
#
#Los datos obtenidos fueron los siguientes:  
#1.18 1.18 1.18 1.18 1.19 1.19 1.19 1.20 1.20 1.20 1.20 1.20 1.21 1.21 1.21 1.22 1.22 1.22 1.22 1.22
#1.23 1.23 1.23 1.23 1.24 1.24 1.24 1.24 1.24 1.25 1.25 1.25 1.25 1.26 1.26 1.26
#1.29 1.29 1.29 1.29 1.30 1.30 1.30 1.31 1.31 1.31 1.31 1.33 1.33 1.34 1.34 1.34   
#
# Comprobar que los datos tengan un comportamiento normal, por medio de una prueba de normalidad,  
# antes de hacer cualquier análisis.  
# Determinar el tamaño de muestra con un nivel de confianza del 80% y considerando que el costo de  
# la producción de cada producto es alta.  
# con ayuda de las tablas military-standard determinar el tamaño de muestra y compara con la de la  
# fórmula; se debe argumentar qué tamaño de muestra se tomó, tomando como referencia las condiciones  
# establecidas en el inciso.  
# Determinar las medidas de tendencia central y de dispersión.  
# Interpretar resultados.

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.power import TTestIndPower

#datos proporcionados
datos = np.array([
    1.18, 1.18, 1.18, 1.18, 1.19, 1.19, 1.19, 1.20, 1.20, 1.20, 1.20, 1.20,
    1.21, 1.21, 1.21, 1.22, 1.22, 1.22, 1.22, 1.22, 1.23, 1.23, 1.23, 1.23,
    1.23, 1.24, 1.24, 1.24, 1.24, 1.24, 1.25, 1.25, 1.25, 1.25, 1.26, 1.26,
    1.26, 1.29, 1.29, 1.29, 1.29, 1.30, 1.30, 1.30, 1.31, 1.31, 1.31, 1.31,
    1.33, 1.33, 1.34, 1.34, 1.34,])

#prueba de normalidad (shapiro.wilk)
shapiro_test = stats.shapiro(datos)
print ("--- prueba de normalidad (shapiro.wilk)---")
print (f"estadistico w: {shapiro_test.statistic}:.4f")
print (f"valor p: {shapiro_test.pvalue:.4f}")
if shapiro_test.pvalue > 0.05:
    print("conclusion: los datos siguen una distribucion normal (p > 0.05).")
else:
        print("conclusion: los datos NO siguen una distribucion normal (p = 0.05).")

# tamaño de muesta (80% de confianza, error estandar bajo por costo alto)
#usando formula para media poblacional: n = (z * s / E)^2
confianza = 0.80
alpha = 1 - confianza
Z = stats.norm.ppf(1 - alpha/2)
sigma = np.std(datos, ddof=1)
E = 0.01
n_formula = (Z * sigma / E) ** 2
print("\n--- tamaño de muestra (formula)---")
print(f"nivel de confianza: {confianza*100}%")
print(f"Z-score: {Z:.4f}")
print(f"desviacion estandar (s): {sigma:.4f}")
print(f"margen de error (E): {E}")
print(f"tamaño de muestra calculado: {np.ceil(n_formula):.0f}")

#comparacion  con MIL-STD-105E (nivel de inspeccion general  II, AQL 1.0%)
#para lote de 52 unidades (similar a los datos), tabla suguiere n=8
print("\n--- comparacion con MIL-STD-105E---")
print("condiciones")
print("-nivel de inspeccion: general II")
print("-AQL: 1.0% (calidad aceptable)")
print("-tamaño de lote: ~50(similar a los datos)")
print("tamaño de muestra segun tabla: n = 8")

#medidas de tendencia central
media = np.mean(datos)
mediana = np.median(datos)
moda = stats.mode(datos, keepdims=True).mode[0]

print("\n--- medidas de tendencia central---")
print("media: {.4f} cm")
print("mediana: {medina:. 4f} cm")
print("moda: {moda:. 4f} cm")

#medidas de dispersion
desviacion_std = np.std(datos,ddof=1)
varianza = np.var(datos,ddof=1)
rango = np.max(datos) - np.min(datos)
rango_intercuartil = stats.iqr(datos)

print("\n---medidas de dispersion---")
print(f"desviacion estandar: {desviacion_std:.4f} cm")
print(f"varianza: {varianza:.4f} cm --")
print(f"rango: {rango:.4f} cm")
print(f"rango intercuartil (IQR): {rango_intercuartil:.4f}")

#visualizacion
plt.figure(figsize=(12, 5))

#historia + curva de densidad
plt.subplot(1, 2, 1)
sns.histplot(datos, kde=True, color='red', bins=10)
plt.title('distribucion de diametro de monedas')
plt.xlabel('diametro (cm)')
plt.xlabel('frecuencia')

#grafico Q-Q
plt.subplot(1, 2, 2)
stats.probplot(datos, plot=plt)
plt.title('grafica Q-Q para normalidad')

plt.tight_layout()
plt.show

#interpretacion
print("\n---interpretacion de resultafos---")
if shapiro_test.pvalue > 0.05:
    print("los datos son normales, se pueden aplicar metodos parametricos.")
else:
    print("-los datos NO son normales, considere pruebas no paametricas.")

print(f"- la media del diametro es {media:.2f} cm. si el estandar es 1.25 cm, hay desviaciones.")
print(f"la desviacion estandar ({desviacion_std:.4f}cm)indica variabilidad en la producion.")
print("posibles causa de efectos:")
print(" * maquina mal calibrada (valores atipicos en 1.18 y 1.34 cm).")
print(" *operador no sigue protocolos (variablidad alta9).")
print("\n---recomendacion---")
print("1. ajustar la maquina para reducir la desviacion estandar.")
print("2. capacitar al operador en controles de calidad.")
print("3. usar tamaño de muestra n=8 (MIL-STD-105E) para futuros lotes (balance entre costo y confianza")
