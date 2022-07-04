from turtle import *
from random import randint # necesitamos importar la función randint del módulo random para generar números enteros aleatorios.


window = Screen()


# La ventana de la tortuga es una cuadrícula xy clásica cuyos ejes x e y van de –300 a 300 por defecto. Limitemos la posición de la tortuga a cualquier lugar entre -200 y 200 para x e y

# Ahora vamos a crear una función llamada wander() para que la tortuga deambule por la pantalla. Para hacer esto, usamos el bucle infinito while True de Python, que siempre se evalúa como True. Esto hará que la tortuga deambule sin parar. Para detenerlo, podemos hacer clic en la X en la ventana de gráficos de la tortuga.

speed(0) # esto hace que la tortuga ande a su mayor velocidad
def wander():
    while True: # cualquier cosa dentro de este loop se ejecutará indefinidamente
        forward(3) # la tortuga avanza tres pasos (o 3 píxeles)
        if xcor() >=200 or xcor() <= -200 or ycor() <= -200 or ycor() >=200:
            left(randint(90, 180)) # y evalúa su posición usando un condicional. Las funciones para la coordenada x y la coordenada y de un tortuga son xcor() y ycor(), respectivamente.


# Usando la sentencia if, le decimos al programa que si alguna de las sentencias condicionales es Verdadera (la tortuga está fuera de la región especificada), haga que la tortuga gire a la izquierda un número aleatorio de grados, entre 90 y 180, para evitar que se extravíe. Si la tortuga está dentro del rectángulo, el condicional se evalúa como Falso y no se ejecuta ningún código. De cualquier manera, el programa regresa a la parte superior del ciclo while True y ejecuta fordward(3) nuevamente.

wander()

window.exitonclick()