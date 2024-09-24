###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     newColor = (r,g,b)
#     rgb_colors.append(newColor)
#
# print(rgb_colors)
from turtle import Turtle, Screen
import turtle as t
import random

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]



george = t.Turtle()
t.colormode(255)

george.shape("turtle")
george.color("turquoise")
george.hideturtle()
george.penup()
george.speed("fastest")
george.setposition(-225,-225)

temp = 0
for y in range(10):
    for x in range(10):
        george.dot(20, random.choice(color_list))
        george.fd(50)
    x = -225
    temp += 50
    y = -225 + temp
    george.setposition(x,y)







screen = Screen()
screen.exitonclick()











