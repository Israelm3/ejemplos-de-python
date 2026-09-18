#Luis fabrica un anuncio luminoso con focos de color rojo, amarillo y verde, de
#tal manera que los focos rojos enciendan cada 10 segundos, los amarillos cada 6
#y los verdes cada 15, si al probar el anuncio encienden juntos los focos a la vez,
#}¿despues de cuantos segundos volveran a encender juntos?

import math
def mcm(a, b ,c):
    #calculamos el mcm de dos numeros usando la relacion mcm(a,b) = (a*b) // mcd(a,b)
    mcm_ab = (a * b)
    mcm_abc = (mcm_ab * c)
    return mcm_abc
# Intervalos de encendido de los focos (en segundo)
rojo = 10
amarillo = 6
verde = 15
# Calculamos el mcm de los tres intervalos
tiempo_simultaneo = mcm(rojo, amarillo, verde)
print(f"Los focos volveran a encender juntos despues de {tiempo_simultaneo} segundos.")
