# Antes de dibujar la forma, primero definimos el tamaño de nuestro cuaderno de bocetos, conocido como plano de coordenadas. 
# En este ejemplo, usamos la función size() para decir que nuestra cuadrícula tendrá 600 píxeles de ancho y 600 píxeles de alto.
# Con nuestro plano de coordenadas configurado, usamos la función de dibujo ellipse() para crear nuestro círculo en este plano. 
# Los dos primeros parámetros, 200 y 100, muestran dónde se encuentra el centro del círculo. Aquí, 200 es la coordenada x y el segundo número, 100, 
# es la coordenada y del centro de este círculo, lo que lo ubica en (200,100) en el plano.
# Los dos últimos parámetros determinan el ancho y el alto de la forma en píxeles. 
# En el ejemplo, la forma tiene 20 píxeles de ancho y 20 píxeles de alto. 
# Debido a que los dos parámetros son iguales, significa que los puntos de la circunferencia son equidistantes del centro, 
# formando un círculo perfectamente redondo.

# El procesamiento tiene una serie de funciones que se pueden utilizar para dibujar formas. 
# Consulta la lista completa en https://processing.org/reference/ para explorar otras funciones para dibujar formas.


def setup(): 
    size(600,600)
    
    
def draw():
    ellipse(200,100,20,20)
