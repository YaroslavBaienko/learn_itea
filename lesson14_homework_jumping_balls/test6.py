import random
import turtle
from screeninfo import get_monitors

MONITOR = get_monitors().pop()
SCREEN_WIDTH = MONITOR.width
SCREEN_HEIGHT = MONITOR.height
BALLS_QUANTITY = 10
BALL_SIZE = (1, 1)


class Ball(turtle.Turtle):
    gravity = -0.001  # pixels/(time of iteration)^2
    energy_loss_ground = 0.95
    energy_loss_walls = 0.8

    def __init__(self, x=0, y=0):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.y_velocity = random.randint(-10, 50) / 10
        self.x_velocity = random.randint(-30, 30) / 10
        self.setposition(x, y)
        self.size = int(random.gammavariate(25, 0.8))
        self.color((random.random(),
                    random.random(),
                    random.random())
                   )
    def draw(self):
        self.clear()
        self.dot(self.size)

    def move(self):
        self.y_velocity += self.gravity
        self.sety(self.ycor() + self.y_velocity)
        self.setx(self.xcor() + self.x_velocity)

    def bounce_floor(self, floor_y):
        if self.ycor() < floor_y:
            self.y_velocity = -self.y_velocity * self.energy_loss_ground
            self.sety(floor_y)

    def bounce_walls(self, wall_x):
        if abs(self.xcor()) > wall_x:
            self.x_velocity = -self.x_velocity * self.energy_loss_walls
            sign = self.xcor() / abs(self.xcor())
            self.setx(wall_x * sign)




window = turtle.Screen()
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)
window.bgcolor('black')
window.title('Balls aquarium')
window.cv._rootwindow.resizable(False, False)
window.onkey(window.bye, 'Escape')
window.listen()

balls = [Ball() for _ in range(BALLS_QUANTITY)]

def add_ball(x, y):
    balls.append(Ball(x, y))

window.onclick(add_ball)

if __name__ == '__main__':
    while True:
        for ball in balls:
            ball.draw()
            ball.move()
            ball.bounce_floor(-SCREEN_HEIGHT/2)
            ball.bounce_walls(SCREEN_WIDTH/2)

        window.update()