from turtle import *
from screeninfo import get_monitors

MONITOR = get_monitors().pop()
SCREEN_WIDTH = MONITOR.width
SCREEN_HEIGHT = MONITOR.height

window = Screen()
window.bgcolor('black')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.listen()
window.tracer(0)

sun = Turtle()
sun.up()
sun.shape('circle')
sun.shapesize(5, 5)
sun.color('yellow')
sun.speed = 0.05
sun.half_size = 50
sun.right_border = SCREEN_WIDTH // 2 - sun.half_size
sun.left_border = -SCREEN_WIDTH // 2 + sun.half_size

while True:
    sun.x = sun.xcor()
    sun.y = sun.ycor()
    sun.goto(sun.x + sun.speed, sun.y)

    if sun.x > sun.right_border:
        sun.setx(sun.right_border)
        sun.speed *= -1

    if sun.x < sun.left_border:
        sun.setx(sun.left_border)
        sun.speed *= -1

    window.update()
