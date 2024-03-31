from turtle import *


def draw_line(point1: list, point2: list):
    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()


Screen().setup(1200, 1200)
shape("turtle")
penup()

draw_line([-500, -250], [-100, -250])
draw_line([-100, -250], [-100, 200])
draw_line([-100, 200], [-300, 200])
draw_line([-300, 200], [-300, 100])
draw_line([-300, 40], [-300, -100])
draw_line([-300, 40], [-240, 0])
draw_line([-300, 40], [-360, 0])
draw_line([-300, -100], [-230, -170])
draw_line([-300, -100], [-370, -170])
mainloop()
