import colorgram
# https://pypi.org/project/colorgram.py/ for more info
# rgb_colors = []
# # Extract 30 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# # print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# # when the tuple members are close to 255, they're closer to white. So we will ignore them
# rgb_colors_new = []
# for tup in rgb_colors:
#     print(f"[0]: {tup[0]}, [1]: {tup[1]}, [2]: {tup[2]}")
#     if (int(tup[0]) > 235 and int(tup[1]) > 235 and int(tup[2]) > 235):
#         print(f"ignoring {tup}")
#     else:
#         rgb_colors_new.append(tup)
# print(f"Dropped {len(rgb_colors) - len(rgb_colors_new)} tuples")
# print(rgb_colors_new)

# rgb_colors_new saved into colorlist. we dont need to run it every time
colorlist = [(202, 164, 110),  (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# requirement : 10 X 10 spots
# each dot to be 20 in size and placed 50 paces apart
import random
import turtle as t
from turtle import Screen
from random import randint, choice
import tkinter as tk
tim = t.Turtle()
t.colormode(255)
tim.shape("circle")
tim.pensize(20)
tim.speed("fastest")
height = 10
width = height
space = 50
xstarter = -200
count = 1
ypos = -200
for i in range(0, height):
    tim.penup()
    xpos = xstarter
    for j in range(0, width):
        color = colorlist[random.randint(0, len(colorlist) - 1)]
        print(f"i: {i}| j: {j} | xpos: {xpos} | ypos: {ypos} | Dot: {count} | Color: {color}")
        tim.goto(xpos, ypos)
        tim.color(color)
        tim.pendown()
        tim.circle(1)
        tim.penup()
        xpos += space
        count += 1
    ypos += space

#the following has to be at the bottom of the code because we need the
# window active until we are done with our coding
screen = Screen()
screen.exitonclick()  # without this, the window will disappear immediately