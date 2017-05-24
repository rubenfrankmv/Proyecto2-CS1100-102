#importar librería
import turtle,time

#creando la ventana
ventana = turtle.Screen()
ventana.title("Mi primera tortuga")
ventana.setup(3840,2160,0,0)

#definir color de fondo
turtle.bgcolor("black")

#definir velocidad de dibujado
turtle.speed(500)

#Primer fractal
turtle.pencolor("white")
for i in range(470):
    turtle.forward(i)
    turtle.right(45)
    turtle.left(990)

turtle.home()
turtle.pos()
(0,0)



colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'pink']
t1=turtle.Pen()
turtle.bgcolor('black')
t1.speed(0)
for x in range(480):
    t1.pencolor(colors[x%7])
    if x%2==0:
        t1.forward(x)
    else:
        t1.backward((x-1))
    t1.left(52)




turtle.penup()
turtle.goto(-640,-315)
turtle.pendown()
for i in range(12):
    turtle.pencolor("white")
    for i in range(30):
        turtle.forward(i)
        turtle.right(145)
turtle.penup()
turtle.goto(610,-315)
turtle.pendown()
for i in range(12):
    turtle.pencolor("white")
    for i in range(30):
        turtle.forward(i)
        turtle.right(145)
turtle.penup()
turtle.goto(610,270)
turtle.pendown()
for i in range(12):
    turtle.pencolor("white")
    for i in range(30):
        turtle.forward(i)
        turtle.right(145)
turtle.penup()
turtle.goto(-640,270)
turtle.pendown()
for i in range(12):
    turtle.pencolor("white")
    for i in range(30):
        turtle.forward(i)
        turtle.right(145)





turtle.penup()
turtle.goto(450,0)
turtle.pendown()



#arreglo para seleccionar el color de la figura
c = ("#5035ED", "red", "#D098D3", "#B2E9F1", "#F8EB39", "#F06A6A", "#B3F87F")
#tamaño de pincel
turtle.pensize(2)
turtle.speed(0)
#funcion que dibuja un cuadrado
def f1(a):
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.left(88)
#funcion recursiva
def fractal(a, b, d):
    if(a>d or b<0):
        return
    if(b==6):
        turtle.color(c[b])
        b=0
    else:
        turtle.color(c[b])
        b=b+1
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.left(90)
    f1(a-1.2)
    fractal(a+1,b, d)
#fractal(tamaño inicial, color(1-6), tamaño final)
fractal(2, 1, 94)

turtle.penup()
turtle.goto(-450,0)
turtle.pendown()



#arreglo para seleccionar el color de la figura
c = ("#5035ED", "red", "#D098D3", "#B2E9F1", "#F8EB39", "#F06A6A", "#B3F87F")
#tamaño de pincel
turtle.pensize(2)
turtle.speed(0)
#funcion que dibuja un cuadrado
def f1(a):
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.left(88)
#funcion recursiva
def fractal(a, b, d):
    if(a>d or b<0):
        return
    if(b==6):
        turtle.color(c[b])
        b=0
    else:
        turtle.color(c[b])
        b=b+1
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.left(90)
    f1(a-1.2)
    fractal(a+1,b, d)
#fractal(tamaño inicial, color(1-6), tamaño final)
fractal(2, 1, 94)
turtle.penup()
turtle.goto(335,70)
turtle.pendown()


for i in range(12):
    turtle.pencolor("skyblue")
    for i in range(30):
        turtle.forward(i)
        turtle.right(199)
        turtle.left(188)

turtle.penup()
turtle.goto(-350,100)
turtle.pendown()

turtle.pencolor("red")
for i in range(1):
    turtle.forward(i)
    turtle.right(117)
    turtle.left(50)
    for i in range(102):
        turtle.forward(i)
        turtle.right(60)

turtle.penup()
turtle.goto(-350,-100)
turtle.pendown()

turtle.pencolor("red")
for i in range(1):
    turtle.forward(i)
    turtle.right(117)
    turtle.left(50)
    for i in range(102):
        turtle.forward(i)
        turtle.right(60)

turtle.penup()
turtle.goto(350,100)
turtle.pendown()

turtle.pencolor("red")
for i in range(1):
    turtle.forward(i)
    turtle.right(117)
    turtle.left(50)
    for i in range(102):
        turtle.forward(i)
        turtle.right(60)


turtle.penup()
turtle.goto(350,-100)
turtle.pendown()

turtle.pencolor("red")
for i in range(1):
    turtle.forward(i)
    turtle.right(117)
    turtle.left(50)
    for i in range(102):
        turtle.forward(i)
        turtle.right(60)

turtle.penup()
turtle.goto(450,-150)
turtle.pendown()
def curva(n):
    """Devuelve una lista de caracteres con los giros
       requeridos para dibujar la curva de dragón de orden
       n. La letra 'I' significa girar a la izquierda,
       mientras que la letra 'D' significa girar a la
       derecha.
    """
    if n == 0:
        return []
    else:
        c = curva(n - 1)
        r = c[::-1]
        i = ['I' if g == 'D' else 'D' for g in r]
        return c + ['I'] + i

for i in range(6):
    print('orden {0}: {1}'.format(i, ''.join(curva(i))))

from turtle import *

def dragon(n, x):
    """Dibuja una curva de dragón de orden n en donde
       cada segmento de la curva es de longitud x.
    """
    fd(x)
    for g in curva(n):
        if g == 'I':
            lt(90)
        else: # g == 'D'
            rt(90)
        fd(x)

hideturtle()
pensize(3)
color('SteelBlue')
speed('fastest')
setheading(180)
dragon(8, 15)



turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()

for i in range(19):
    turtle.pencolor("blue")
    for i in range(30):
        turtle.forward(i)
        turtle.right(177)
        turtle.left(150)


turtle.penup()
turtle.goto(300,300)
turtle.pendown()
for i in range(17):
    turtle.pencolor("blue")
    for i in range(30):
        turtle.forward(i)
        turtle.right(29)

turtle.penup()
turtle.goto(250,-250)
turtle.pendown()

turtle.pencolor("red")
for i in range(2):
    turtle.forward(i)
    turtle.right(117)
    turtle.left(51)
    for i in range(150):
        turtle.forward(i)
        turtle.right(199)
        turtle.left(23)

turtle.penup()
turtle.goto(-300,300)
turtle.pendown()

turtle.pencolor("pink")
def Nieve(lado, n):
    if n==0:
        turtle.forward(lado)
    else:
        lado = lado/3
        Nieve(lado, n-1)
        turtle.left(60)
        Nieve(lado, n-1)
        turtle.right(120)
        Nieve(lado, n-1)
        turtle.left(60)
        Nieve(lado, n-1)

Nieve(1000,4)



turtle.penup()
turtle.goto(0,300)
turtle.pendown()


turtle.pencolor("skyblue")

loadWindow = turtle.Screen()
stacy = turtle.Pen()
stacy.speed(0)
stacy.penup()
stacy.goto(0, -100)
stacy.pendown()

def draw_fractal(length, depth):
    stacy.forward(length)
    if depth > 1:
        stacy.backward(length/2)
        stacy.left(90)
        draw_fractal(length/2.1, depth-1)
        stacy.right(180)
        draw_fractal(length/2.1, depth-1)
        stacy.right(90)
        stacy.forward(length/2)
    stacy.right(180)
    stacy.forward(length)

draw_fractal(400,8)
stacy.right(180)
draw_fractal(400,8)


turtle.penup()
turtle.goto(-350,-350)
turtle.pendown()
for i in range(17):
    turtle.pencolor("blue")
    for i in range(30):
        turtle.forward(i)
        turtle.right(185)
        turtle.left(77)


#termina la gráfica
turtle.done()
