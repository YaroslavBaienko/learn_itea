from tkinter import Tk
import tkinter as tk

from cross_game.settings.game_settings import FONT


class GameOverWin(Tk):
    def __init__(self, help_text: str = ''):
        super(GameOverWin, self).__init__()
        self.title('Game over')
        self.geometry('500x250+700+270')
        self.attributes("-topmost", True)
        self.text = tk.Text(self, width=500, height=500, bg="blue",
                            fg='white', wrap=tk.WORD, font=FONT)
        self.help_text = help_text

    def set_text(self):
        self.text.insert(1.0, self.help_text)
        self.text['state'] = tk.DISABLED
        self.text.pack()
        self.mainloop()

