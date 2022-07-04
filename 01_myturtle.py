import turtle
window = turtle.Screen()
turtle.delay(100)

# t = turtle.Turtle()
t = turtle.Pen()


# UNO
# t.shape('turtle')
# t.forward(100)

# As you can see, the turtle started in the middle of the screen and walked forward 100 steps (it’s actually 100 pixels). Notice that the default shape is an arrow, not a turtle, and the default direction the arrow is facing is to the right. To change the arrow into a turtle, update your code so that it looks like this: UNO

# As you can probably tell, shape() is another function defined in the turtle module. It lets you change the shape of the default arrow into other shapes, like a circle, a square, or an arrow.

# CHANGING DIRECTIONS

# t.right(45) 
# t.forward(150)


# EXERCISE 1-­1: SQUARE DANCE 
# Your first challenge is to modify the code in the program using only the forward and right functions so that the turtle draws a square.

# CUADRADO

# t.forward(100)
# t.right(90) 
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

# OCTOGONO

t.forward(100)
t.right(45) # ¿Este ángulo es el interior o el exterior?
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)






window.exitonclick()