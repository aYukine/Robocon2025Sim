from settings import *
from robot import Robot
pg.init()

class Simulation:
    def __init__(self):
        self.win = pg.display.set_mode(game_field_size)
        self.run = True
        self.robot1 = Robot(40, 40, robot_d, RED)

    def draw_robots(self):
        self.robot1.draw_robot(self.win)

    def mainloop(self):
        while self.run:
            for events in pg.event.get():
                if events.type == pg.QUIT:
                    self.run = False

            self.win.blit(game_field_img, (0, 0)) # this is the background
            self.draw_robots()

            pg.display.update()

def main():
    game = Simulation()
    game.mainloop()

if __name__ == "__main__":
    main()