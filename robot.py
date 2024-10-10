import pygame as pg
import numpy as np

class Robot:
    def __init__(self, x, y, diameter, color):
        self.x = x
        self.y = y
        self.radius = diameter/2
        self.possesion = False
        self.color = color
        self.rect = pg.Rect(x-diameter/2, y-diameter/2, diameter, diameter)
        self.speed = 10

    def update_rect(self):
        self.rect = pg.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)

    def move(self, desired_x, desired_y):
        current_pos = np.array([self.x, self.y])
        target_pos = np.array([desired_x, desired_y])
        direction = target_pos - current_pos
        distance_squared = np.sum(direction ** 2)

        if distance_squared > self.speed ** 2:
            direction_normalized = direction / np.linalg.norm(direction)
            movement_vector = direction_normalized * self.speed
        else:
            movement_vector = direction

        self.x += movement_vector[0]
        self.y += movement_vector[1]

        if np.array_equal(movement_vector, [0, 0]):
            return True
        return False
    
    def draw_robot(self, win):
        pg.draw.circle(win, self.color, (self.x, self.y), self.radius)