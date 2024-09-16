from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("turquoise")

#------------------------Square Turtle-----------------------------------

# turtle draw a square

# def square(x):
#     for i in range(4):
#         timmy_the_turtle.forward(x)
#         timmy_the_turtle.right(90)
#square(100)

#--------------------------Dotted Line Turtle-----------------------------

# turtle will draw a dotted line and can specify how long it is.

# def draw():
#     if not timmy_the_turtle.down():
#         timmy_the_turtle.down()
#         timmy_the_turtle.forward(10)
#     else:
#         timmy_the_turtle.forward(10)
#
# def gap():
#     if not timmy_the_turtle.up():
#         timmy_the_turtle.up()
#         timmy_the_turtle.forward(10)
#     else:
#         timmy_the_turtle.forward(10)
#
# for x in range(50):
#     draw()
#     gap()

#------------------------------Shape Turtle-------------------------------

# turtle can draw any n sided shape with l length. Specify the parameters.
# Within the for loop turtle can stack drawn shape. Each shape a random color chosen

# color = ["DarkGreen","burlywood4","CadetBlue","cornsilk","DarkOrchid4",
#          "hotpink", "navy","tomato4", "SeaGreen4", "VioletRed4"]
#
# def draw_shape(n_side, l_side, color):
#     for x in range(n_side):
#         angle = 180 - ((n_side-2) * (180/n_side))
#         timmy_the_turtle.color(color)
#         timmy_the_turtle.forward(l_side)
#         timmy_the_turtle.right(angle)
#
# for x in range(3,11):
#     c = random.choice(color)
#     draw_shape(x,100, c)


screen = Screen()
screen.exitonclick()















screen = Screen()
screen.exitonclick()
