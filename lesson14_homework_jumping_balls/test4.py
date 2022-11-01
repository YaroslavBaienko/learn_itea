import turtle, random

# window = turtle.Screen()
# border = turtle.Turtle()
# border.speed(0)
# border.up()
# border.hideturtle()
# border.pensize(5)
# border.color('red')
# border.goto(300,300)
# border.down()
# border.goto(300,-300)
# border.goto(-300,-300)
# border.goto(-300,300)
# border.goto(300,300)

ball = turtle.Turtle()
ball.hideturtle()
ball.shape('circle')
ball.up()
randx = random.randint(-290,290)
randy = random.randint(-290,290)
ball.goto(randx,randy)
ball.showturtle()
dx = 3
dy = 2

while True:
    x,y = ball.position()
    if x+dx >=300 or x+dx <= -300:
        dx = -dx
    if y+dy >=300 or y+dy <= -300:
        dy = -dy
    ball.goto(x+dx, y+dy)

window.mainloop()