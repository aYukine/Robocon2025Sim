import pygame as pg
import math
# game setting 
FPS = 30

# dimension and placement 
# size factor is of 1/10 of original
game_field_size = (1500, 800)
robot_d = 80
robot1_x, robot1_y = 100, 200
robot2_x, robot2_y = 300, 500
robot3_x, robot3_y = 1400, 600
robot4_x, robot4_y = 1200, 300
robot_speed = 200 #pixel per second = 3 meter per second
rotation_speed = 180
shoot_speed = 300

dribble_time = 0.3 # 1 second

hand_length = 30
hand_width = 10

# color
RED = (255, 10, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (10, 10, 255)
GREY = (200, 200, 200)
GREEN = (10, 202, 10)

# assets loading
# game_field_img = pg.transform.scale(pg.image.load("assets/gameField.png"), (1504, 802)).convert_alpha()
