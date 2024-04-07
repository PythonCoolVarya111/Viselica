from turtle import *


def draw_line(point1, point2, size=3, p_color='black') -> object:
    oldpensize = pen()[('pensize')]
    oldcolor = pen()['pencolor']
    pensize(size)
    pencolor(p_color)
    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()
    pensize(oldpensize)
    pencolor(oldcolor)


def draw_circle(radius, size=3, p_color='black'):
    oldpensize = pen()['pensize']
    oldcolor = pen()['pencolor']
    pensize(size)
    pencolor(p_color)
    pendown()
    circle(radius)
    penup()
    pensize(oldpensize)
    pencolor(oldcolor)


def draw_square(top_left, len_edge, size=3, p_color='black'):
    x = top_left[0]
    y = top_left[1]
    points = [x, y], [x+len_edge, y], [x+len_edge, y - len_edge], [x, y - len_edge]
    draw_line(points[0], points[1], size, p_color)
    draw_line(points[1], points[2], size, p_color)
    draw_line(points[2], points[3], size, p_color)
    draw_line(points[3], points[0], size, p_color)


Screen().setup(1200, 900)


shape("turtle")
speed(0)
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
goto(-300, 40)
draw_circle(31)
penup()
draw_square([-400, -300], 100)
mainloop()
