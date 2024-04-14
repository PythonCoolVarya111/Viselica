from turtle import *

#функции:

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

def draw_square(top_left, len_edge = 60, size=3, p_color='black'):
    x = top_left[0]
    y = top_left[1]
    points = [x, y], [x+len_edge, y], [x+len_edge, y - len_edge], [x, y - len_edge]
    draw_line(points[0], points[1], size, p_color)
    draw_line(points[1], points[2], size, p_color)
    draw_line(points[2], points[3], size, p_color)
    draw_line(points[3], points[0], size, p_color)

def draw_zagadka(word):
    lenSquare = 60
    interval = 35
    screenWidth = Screen().window_width()
    wordWidth = (len(word) * lenSquare) + (len(word) - 1) * interval
    x = (screenWidth // 2 * -1) + (screenWidth - wordWidth) // 2
    startPoint = [x, -300]
    for x in range(len(word)):
        draw_square(startPoint, lenSquare + 20)
        startPoint[0] += lenSquare + interval

def draw_alphabet():
    x = 100
    y = 250
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    alphabet_dict = {}
    for i in range(len(alphabet)):
        if i % 5 == 0 and i != 0:
            x = 100
            y -= 80
        goto(x, y)
        write(alphabet[i], align='center', font=('Comic Sans MS', 40, 'bold' ))
        alphabet_dict[alphabet[i]] = (xcor(), ycor()+30)
        x += 100


#экран

Screen().setup(1200, 900)


#отображение черепашки:

shape("turtle")
speed(3)
penup()


#рисуем человека и виселицу:

draw_line([-500, -250], [-100, -250])
draw_line([-100, -250], [-100, 200])
draw_line([-100, 200], [-300, 200])
draw_line([-300, 200], [-300, 100])
goto(-300, 40)
draw_circle(31)
penup()
draw_line([-300, 40], [-300, -100])
draw_line([-300, 40], [-240, 0])
draw_line([-300, 40], [-360, 0])
draw_line([-300, -100], [-230, -170])
draw_line([-300, -100], [-370, -170])



#рисуем квадраты для слова:

draw_zagadka('fgfa')


#пишем алфавит:

draw_alphabet()


mainloop()
