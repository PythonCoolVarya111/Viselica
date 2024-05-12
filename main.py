import random
from words import word
from turtle import *

# global
alphabet_dict = {}
squareCoods = []
countErrors = 0
vibor = random.choice(word)
score = 0
scorewin = len(vibor)

# функции:

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


def draw_square(top_left, len_edge=60, size=7, p_color='black'):
    x = top_left[0]
    y = top_left[1]
    points = [x, y], [x + len_edge, y], [x + len_edge, y - len_edge], [x, y - len_edge]
    draw_line(points[0], points[1], size, p_color)
    draw_line(points[1], points[2], size, p_color)
    draw_line(points[2], points[3], size, p_color)
    draw_line(points[3], points[0], size, p_color)


def draw_zagadka(word):
    global squareCoods
    lenSquare = 80
    interval = 35
    screenWidth = Screen().window_width()
    wordWidth = (len(word) * lenSquare) + (len(word) - 1) * interval
    squareCoods = []
    x = (screenWidth // 2 * -1) + (screenWidth - wordWidth) // 2
    startPoint = [x, -300]
    for x in range(len(word)):
        draw_square(startPoint, lenSquare)
        squareCoods.append([startPoint[0] + (lenSquare // 2), startPoint[1] - lenSquare])
        startPoint[0] += lenSquare + interval
    print(squareCoods)


def draw_alphabet():
    global alphabet_dict
    x = 100
    y = 250
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    for i in range(len(alphabet)):
        if i % 5 == 0 and i != 0:
            x = 100
            y -= 80
        goto(x, y)
        write(alphabet[i], align='center', font=('Comic Sans MS', 40, 'bold'))
        alphabet_dict[alphabet[i]] = (xcor(), ycor() + 30)
        x += 100


def button_alphabet(x, y):
    global alphabet_dict
    for key, centerCoord in alphabet_dict.items():
        if abs(centerCoord[0] - x) < 100 // 2 and abs(centerCoord[1] - y) < 80 // 2:
            print(key)
            goto(alphabet_dict.pop(key))
            dot(80, 'white')
            check_letter(key.lower())
            break


# функция отрисовки человека и виселицы:
def draw_error(numError):
    match numError:
        case 1:
            draw_line([-500, -250], [-100, -250])
        case 2:
            draw_line([-100, -250], [-100, 200])
        case 3:
            draw_line([-100, 200], [-300, 200])
        case 4:
            draw_line([-300, 200], [-300, 100])
        case 5:
            goto(-300, 40)
            draw_circle(31)
            penup()
        case 6:
            draw_line([-300, 40], [-300, -100])
        case 7:
            draw_line([-300, 40], [-240, -5])
        case 8:
            draw_line([-300, 40], [-360, 0])
        case 9:
            draw_line([-300, -100], [-230, -170])
        case 10:
            draw_line([-300, -100], [-370, -170])
            print('You are LOSE')
            clear()


def check_game(scorewin, score, numError):
    if score == scorewin:
        print('ПОБЕДА')
    elif numError == 10:
        lose()

def check_letter(letter):
    global countErrors
    global vibor
    global score
    if letter in vibor:
        for i in range(len(vibor)):
            if vibor[i] == letter:
                goto(squareCoods[i])
                write(letter.upper(), align='center', font=('Comic Sans MS', 50, 'bold'))
                score += 1
        print(score)
    else:
        countErrors += 1
        draw_error(countErrors)
    check_game(scorewin, score, countErrors)


def lose():
    alphabet_dict.clear()
    clear()
    goto(0, 200)
    pencolor('red')
    write('ТЫ ПРОИГРАЛ!', align='center', font=('Comic Sens MS', 55,'bold'))
    pencolor('black')
    goto(0, 0)
    write('Загаданное слово:', align='center', font=('Comic Sens MS', 30,'bold'))
    goto(0, -100)
    write(vibor, align='center', font=('Comic Sens MS', 55,'bold'))
    goto(0, -300)
    write('Желаете продолжить?', align='center', font=('Comic Sens MS', 55,'bold'))
    goto(-200, -400)
    pencolor('green')
    write('ДА', align='center', font=('Comic Sens MS', 55,'bold'))
    goto(200, -400)
    pencolor('red')
    write('НЕТ', align='center', font=('Comic Sens MS', 55,'bold'))


# экран

Screen().setup(1200, 900)

# отображение черепашки:

shape("turtle")
speed(0)
penup()

# рисуем квадраты для слова:

draw_zagadka(vibor)

# пишем алфавит:

draw_alphabet()
onscreenclick(button_alphabet)
mainloop()
