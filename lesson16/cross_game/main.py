import time
import os
import pygame
from pathlib import Path
from tkinter import messagebox

from cross_game import assets
from cross_game.game_lib.sprites.player import Player
from cross_game.game_lib.manager.car_manager import CarManager
from cross_game.game_lib.labels.scoreboard import Scoreboard
from cross_game.game_lib.labels.pause import PauseLabel
from cross_game.game_lib.windows.game_over import GameOverWin
from cross_game.game_lib.windows.enter_name import EnterNameWin
from cross_game.game_lib.windows.main import Window


class Game:
    PATH_TO_ASSETS = str(Path(assets.__file__).parent.absolute())
    PATH_TO_BGPIC = os.path.join(PATH_TO_ASSETS, 'image', 'road.png')
    pause = False

    def __init__(self):
        if self.begin_game():
            pygame.mixer.pre_init(44100, -16, 2, 512)
            pygame.init()
            self.level_song = pygame.mixer.Sound(os.path.join(self.PATH_TO_ASSETS, 'sound', 'level.ogg'))

            login_window = EnterNameWin()
            self.login = login_window.login.title()

            self.window = Window()
            self.window.canvas.bgpic(Game.PATH_TO_BGPIC)

            self.player = Player()
            self.pause_label = PauseLabel()
            self.car_manager = CarManager()
            self.score = Scoreboard()
            self.score.update_scoreboard(self.login)
            self.window.canvas.onkeypress(self.player.move, "Up")
            self.window.canvas.onkeypress(self.set_pause, "p")

    def set_pause(self):
        if self.pause:
            self.pause = False
            self.player.pause = False
            self.car_manager.pause = False
            self.pause_label.clear()
        else:
            self.pause = True
            self.player.pause = True
            self.car_manager.pause = True
            self.pause_label.update_pause()

    def run(self):
        game_is_on = True

        while game_is_on:
            time.sleep(0.05)
            self.window.canvas.update()

            self.car_manager.make_car()
            self.car_manager.move()

            for car in self.car_manager.all_cars:
                if self.player.distance(car) < 20:
                    self.score.game_over()
                    game_is_on = False

            if self.player.is_at_finish_line():
                self.play_sound()
                self.player.go_to_start()
                self.car_manager.increase_speed()
                self.score.update_scoreboard(self.login)

        self.game_over()

    def play_sound(self):
        pygame.mixer.Sound.play(self.level_song)

    def game_over(self):
        game_over_text = f"""
        Game Over!
        Player: {self.login.title()}
        Level: {self.score.current_level}
        """
        game_over = GameOverWin(game_over_text)
        game_over.protocol("WM_DELETE_WINDOW", exit)
        game_over.set_text()

    @classmethod
    def begin_game(cls):
        begin = messagebox.askquestion('Begin game', 'Play now?')
        if begin == 'no':
            exit()
        else:
            return True


if __name__ == '__main__':
    game = Game()
    game.run()
