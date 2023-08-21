import turtle as t
import random

t.shape('turtle')
t.bgcolor("black")


#반복문 도형
ang = 99

t.color("red")
t.speed(0)

for x in range(300):
    t.forward(x)
    t.right(ang)


#별 그리기
color = ("red", "orange", "blue", "green", "pink")

t.color(random.choice(color))
t.begin_fill()

for i in range(5):
    t.forward(100)
    t.left(144)
t.end_fill()


#이름
t.color("yellow")

t.hideturtle()
t.write("김도연", move=False, align="center", font=("arial", 50, "bold"))
t.penup()
t.sety(-100)
t.pendown

t.done()
