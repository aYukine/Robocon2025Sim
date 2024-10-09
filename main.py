import pygame as pg
from settings import *

pg.init()

class Simulation:
    def __init__(self):
        self.win = pg.display.set_mode(game_field_size)
        self.run = True

    def mainloop(self):
        while self.run:
            for events in pg.event.get():
                if events.type == pg.QUIT:
                    self.run = False

            pg.display.update()

def main():
    game = Simulation()
    game.mainloop()

if __name__ == "__main__":
    main()