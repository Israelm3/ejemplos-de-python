#el objetivo de este codigo es visualizar y comparar dos conjuntos de puntos
#tridimensionales (3D) en un grafico de dispersion 3D,utilizando colores
#distintos para diferenciar los grupos. esto permite analizar la distribucion
#espacial, agrupamientos o patrones entre los datos.


#escenario posible:
#un investigador o analista de datos quiere estudiar la relacion emtre tres
#variables numericas en dos grupos diferenhtes (por ejemplo, grupo A y gripo B)


#importamos las librerias necesarias
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

#creamos la figura
fig = plt.figure()
#creamos el plano 3D
ax1 = fig.add_subplot(111, projection='3d')

#definimos los datos de prueba
x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]

#datos adicionales
x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-5,-6,-7,-8,-2,-5,-6,-3,-7,-2]
z2 = [1,2,6,3,2,7,3,3,7,2]

#agregamos los puntos en el plano 3D
ax1.scatter(x, y, z, c='g', marker='o')
ax1.scatter(x2, y2, z2, c='r', marker='o')

#mostramos el grafico
plt.show()

#interpretacion del grafico
#patrones especiales

#si los puntos verdes y rojos se agrupán en zonas distintas, sugiere
#diferencias entre los grupos.
