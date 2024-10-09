import pygame as pg

# dimension and placement 
# size factor is of 1/10 of original
game_field_size = (1500, 800)
robot_d = 80

# color
RED = (255, 10, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# assets loading
game_field_img = pg.transform.scale(pg.image.load("assets/gameField.png"), (1504, 802))


# set strat
