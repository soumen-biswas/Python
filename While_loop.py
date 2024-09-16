'''
n=int(input("Enter a number: "))

m=1
while m<=10:
    print(n, "x", m, "=", n*m)
    m+=1
'''

import turtle

turtle.color("Red")
turtle.speed(2)

counter = 0
while counter<36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter+=1


turtle.exitonclick()

'''
import turtle

height = 5
width = 5

turtle.speed(2)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()
'''
'''
while True:
    n=int(input("Enter a number (0 to exit): "))
    if n==0:
        break
    print("Square of", n, "is", n*n)
'''