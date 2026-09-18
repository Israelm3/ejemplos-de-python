import numpy as np
import matplotlib.pyplot as plt

#datos
x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2

#grafico de lineas
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

##################

### color de linea

import numpy as np
import matplotlib.pyplot as plt

#### datos
x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2

#grafico de lineas
fig, ax = plt.subplots()
ax.plot(x, y, color = "r")
plt.show()

############

###### grosor de la linea

import numpy as np
import matplotlib.pyplot as plt

####datos
x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2

###grafico de lineas
fig, ax = plt.subplots()
ax.plot(x, y, linewidth = 4)
####ax.plot(x, y, 1w =4) ## eqivalente
plt.show()
 #######

###estilo de linea

import numpy as np
import matplotlib.pyplot as plt
#### datos
x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2


####grafico de lineas
fig, ax = plt.subplots()
ax.plot(x, y, linestyle = "--")

##ax.plot(x, y, ls = "--") ##eqivalente
plt.show()


#############
## agregar simbolo a las lineas

import numpy as np
import matplotlib.pyplot as plt

##datos
x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2

####grafico de lineas
fig, ax = plt.subplots()
ax.plot(x, y, marker = "o", markesize = 5)
#ax.plot()x, y, marker = "o", ms = 5) ##equivalente
plt.show()

########
### lineas y simbolos con colores
import numpy as np
import matplotlib.pyplot as plt

####datos
x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2

####grafico de lineas
fig, ax = plt.subplots()
ax.plot(x, y, color = "r", marker = "s",
        markerfacecolor = 'black', markeredgecolor = 'black')
#ax.plot()x, y, color = "r", marker = 's', mfc = 'black', mec = 'black') ##equivalente
plt.show()

###### usar formato
import numpy as np
import matplotlib.pyplot as plt

##datos
x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2

####grafico de lineas
fig, ax = plt.subplots()
ax.plot(x, y, "*g")    
plt.show()


####### grafica con varias lineas

import numpy as np
import matplotlib.pyplot as plt

##datos

x1 = np.linspace(0, 10, 25)
y1 = np.sin(x) + x/2

x2 = np.linspace(0, 10, 25)
y2 = np.cos(x) + x/2

###grafico de lineas
fig, ax = plt.subplots()
ax.plot(x1, y1, marker = "o", label = "sin(x) + x/2")
ax.plot(x2, y2, marker = "o", label = "cos(x) + x/2")
ax.legend()
plt.show()


######## grafica de varios niveles
import numpy as np
import matplotlib.pyplot as plt

##datos

x1 = np.linspace(0, 10, 25)
y1 = np.sin(x) + x/2

x2 = np.linspace(0, 10, 25)
y2 = np.cos(x) + x/2


#####grafico de lineas
fig, ax = plt.subplots()
ax.plot(x1, y1, "c^", x2, x2, "d--")
plt.show()

######funcion steep

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2

#####grafico de lineas
fig, ax = plt.subplots()
ax.step(x, y)
plt.show()
