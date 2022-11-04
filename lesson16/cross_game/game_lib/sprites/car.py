from cross_game.game_lib.sprites.base_sprite import Sprite
from cross_game.settings.game_settings import STARTING_MOVE_DISTANCE


class Car(Sprite):
    move_increment = 0

    def __init__(self):
        super().__init__('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.showturtle()

    def move(self):
        self.backward(STARTING_MOVE_DISTANCE + self.move_increment)
