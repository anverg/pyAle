## https://docs.python.org/3/library/turtle.html#module-turtle


import turtle
window = turtle.Screen()
# turtle.delay(25)

# t = turtle.Turtle()
t = turtle.Pen()


t.shape('turtle')


### CUADRADO CON FOR LOOP

# for i in range(4):
#     t.forward(100)
#     t.right(90)


## EXERCISE 1-2: SQUARE SPIRAL 
## Your second challenge is to modify the code in the program using only the forward and left functions so that the turtle draws a square spiral.

# for i in range(100):
#     t.forward(i)
#     t.left(90)


### CREATING SHORTCUTS WITH FUNCTIONS

## Ahora que hemos escrito el código para dibujar un cuadrado, podemos guardar todo ese código en una palabra clave mágica a la que podemos llamar en cualquier momento en el que queramos usar ese cuadrado de nuevo. Es lo que se llama escribir una FUNCIÓN

## Para definir una función hay que:
## - usar el comando def seguido del nombre que queramos asignar a la función y ()
## - escribir lo que queramos que la función haga

def square():
    for i in range(4):
        t.forward(100)
        t.right(90)

## Para que la función se ejecute, hay que llamarla
square()

## También podemos usar esta función en un bucle para construir algo más complicado. Por ejemplo, para dibujar un cuadrado, girar un poco a la derecha, hacer otro cuadrado, girar un poco a la derecha, y repetir esos pasos varias veces, tiene sentido poner la función dentro de un bucle.

## EXERCISE 1­-3: A CIRCLE OF SQUARES Write and run a function that draws 60 squares, turning right 5 degrees after each square. Use a loop! 


# for i in range(60):
#     square()
#     t.right(5)


## USAR VARIABLES

## Hasta ahora todos nuestros cuadrados son del mismo tamaño. Para hacer cuadrados de diferentes tamaños, necesitaremos variar la distancia que camina la tortuga hacia adelante para cada lado. En lugar de cambiar la definición de la función square() cada vez que queremos un tamaño diferente, podemos usar una variable, que en Python es una palabra que representa un valor que puedes cambiar. Esto es similar a la forma en que x en álgebra puede representar un valor que puede cambiar en una ecuación. En la clase de matemáticas, las variables son letras sueltas, pero en programación puedes dar a una variable el nombre que quieras

## ¿COMO USAMOS VARIABLES EN LAS FUNCIONES?

## Cuando defines una función, puedes usar variables como parámetros de la función dentro de los paréntesis.

# def square(sidelength): 
#     for i in range(4): 
#         t.forward(sidelength)
#         t.right(90)

# square(50)
# square(80)
# square()

## Para evitar el error, podemos dar a la variable (parámetro) un valor por defecto

def square(sidelength=100): 
    for i in range(4): 
        t.forward(sidelength)
        t.right(90)

# square(50)
# square(80)
# square()


### EXERCISE 1-­4: TRI AND TRI AGAIN 
## Write a triangle() function that will draw a triangle of a given “side length.”

## Ver Triangulo.png

# def triangle(sidelength = 100):
#     for i in range(3):
#         t.forward(sidelength)
#         t.right(60)

## That looks like we’re starting to draw a hexagon (a six­sided polygon), not a triangle. We get a hexagon instead of a triangle because we entered 60 degrees, which is the internal angle of an equilateral triangle. We need to enter the external angle to the right() function instead, because the turtle turns the external angle, not the internal angle. This wasn’t a problem with the square because it just so happens the internal angle of a square and the external angle are the same: 90 degrees.

## To find the external angle for a triangle, simply subtract the internal angle from 180. This means the external angle of an equilateral triangle is 120 degrees.


# def triangle(sidelength = 100):
#     for i in range(3):
#         t.forward(sidelength)
#         t.left(120)

# triangle()


## EXERCISE 1­-5: POLYGON FUNCTIONS Write a function called polygon that takes an integer as an argument and makes the turtle draw a polygon with that integer’s number of sides.

# def polygon(sides, sidelength=100):
#     for i in range(sides):
#         t.forward(sidelength)
#         t.left(360/sides)

# polygon(12)

t.speed(0) #this line makes the turtle go faster

def squareCircle():
    '''Draws a circle of squares'''
    for i in range(60):
        square(200)
        t.right(5)

# squareCircle()

## COMO HACER QUE LAS VARIABLES VARÍEN

## Abrir el shell y hacer las siguientes operaciones
radio = 10
radio = 20 # el valor de la variable radio ha cambiado a 20

x = 12
y = 3
x += y

## Ver el valor de x y de y
x += 2
x -= 1
x *= 2
x /= 4

## Puedes usar el siguiente código para incrementar en 5 el valor de la variable length

## length += 5


## EXERCISE 1­5: TURTLE SPIRAL 
## Make a function to draw 60 squares, turning 5 degrees after each square and making each successive square bigger. Start at a length of 5 and increment 5 units every square.

# def turtleSpiral(sidelength=5):
#     # length = 5
#     for i in range(60):
#         square(sidelength)
#         t.right(5)
#         sidelength += 5

# turtleSpiral()



window.exitonclick()