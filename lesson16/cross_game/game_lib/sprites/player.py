from cross_game.game_lib.sprites.base_sprite import Sprite
from cross_game.settings.game_settings import MOVE_DISTANCE, STARTING_POSITION, FINISH_LINE_Y


class Player(Sprite):
    def __init__(self):
        super().__init__('turtle')
        self.pause = False
        self.setheading(90)
        self.color('salmon')
        self.go_to_start()
        self.showturtle()

    def move(self):
        if not self.pause:
            self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
