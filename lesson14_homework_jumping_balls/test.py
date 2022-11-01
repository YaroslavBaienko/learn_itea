import random
from random import randint
from turtle import *
from screeninfo import get_monitors

MONITOR = get_monitors().pop()
SCREEN_WIDTH = MONITOR.width
SCREEN_HEIGHT = MONITOR.height
colors = ['red', 'yellow', 'blue', 'green', 'white', 'pink']
BALLS_QUANTITY = 10
BALL_SIZE = (1, 1)


def make_window():
    """Make window and settings"""
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.title('Balls aquarium')
    screen.cv._rootwindow.resizable(False, False)
    screen.onkey(screen.bye, 'Escape')
    screen.listen()
    screen.tracer(0)
    return screen


class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self)


def make_ball(ball_color: str, ball_size: tuple):
    """Make ball"""
    ball = Turtle(shape='circle')
    ball.hideturtle()
    ball.color(ball_color)
    ball.shapesize(*ball_size)
    ball.penup()
    ball.up()
    random_x = random.randint(-int(SCREEN_WIDTH/2), int(SCREEN_WIDTH/2))
    random_y = random.randint(-int(SCREEN_HEIGHT/2), int(SCREEN_HEIGHT/2))
    ball.goto(random_x, random_y)
    ball.showturtle()
    return ball


window = make_window()

balls = []
for i in range(BALLS_QUANTITY):
    balls.append(make_ball(random.choice(colors), BALL_SIZE))


x, y = 0, 0
xdir, ydir = 3, 3

def ball_move(ball):
    global x, y, xdir, ydir
    xlimit = SCREEN_WIDTH / 2
    ylimit = SCREEN_HEIGHT / 2
    while True:
        x = x + xdir
        y = y + ydir

        if not -xlimit < x < xlimit:
            xdir = -xdir
        if not -ylimit < y < ylimit:
            ydir = -ydir

        ball.goto(x, y)




if __name__ == '__main__':
    window = make_window()
    for ball in balls:
        ball_move(ball)
window.mainloop()


