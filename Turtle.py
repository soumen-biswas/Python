'''
import turtle
#new screen
windos=turtle.Screen()
turtle.bgcolor("white")

#colour in triangle
turtle.color("red")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.pendown()


turtle.shape('turtle')
turtle.speed(2)
for i in range(3):
    turtle.forward(250)
    turtle.left(120)

windos.exitonclick()
'''

'''
import turtle
turtle.speed(2)
for i in range(21):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick()
'''

'''
import turtle

turtle.shape('turtle')
turtle.speed(2)

for i in range(50,101,10):
    for j in range(4):
        turtle.forward(i)
        turtle.left(90)

turtle.exitonclick()
'''