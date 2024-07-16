# import colorgram
#
# image_colors = colorgram.extract("image.jpg", 30)
#
# picked_colours = []
#
# for colour in image_colors:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     picked_colours.append(new_colour)


import tkinter
from turtle import Turtle, Screen
import random

color_list = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)


tim.up()
tim.hideturtle()
x = -225
y = -225
tim.goto(x, y)

for row in range(10):
    for column in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
    y += 50
    tim.goto(x, y)

screen.getcanvas().postscript(file="color_dots.png")

screen.exitonclick()


