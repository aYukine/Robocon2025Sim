import pygame as pg
import numpy as np

class Robot:
    def __init__(self, x, y, diameter, color, speed):
        self.x = x
        self.y = y
        self.radius = diameter/2
        self.possesion = False
        self.color = color
        self.rect = pg.Rect(x-diameter/2, y-diameter/2, diameter, diameter)
        self.speed = speed

    def update_rect(self):
        self.rect = pg.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)

    def move(self, desired_x, desired_y, dt):
        current_pos = np.array([self.x, self.y])
        target_pos = np.array([desired_x, desired_y])
        direction = target_pos - current_pos
        distance = np.linalg.norm(direction) # Calculate the actual distance, not squared

        if distance > self.speed * dt:  # Check against distance covered in time dt
            direction_normalized = direction / distance
            movement_vector = direction_normalized * self.speed * dt # Scale by dt
        else:
            movement_vector = direction

        self.x += movement_vector[0]
        self.y += movement_vector[1]
        self.update_rect()

        if np.array_equal(movement_vector, [0, 0]):
            return True  # Reached destination
        return False # Still moving
    
    def dribble(self):
        pass
    
    def passing(self):
        pass

    def shoot(self):
        pass

    def dunk(self):
        pass
    
    def draw_robot(self, win):
        pg.draw.circle(win, self.color, (self.x, self.y), self.radius)


class ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.rect = pg.Rect(x-radius, y-radius, radius*2, radius*2)
        self.momentum = 0
        self.direction = (0, 0)
        self.attached = False
        self.master = None

    def update_rect(self):
        self.rect = pg.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)

    def move(self):
        if not self.attached:
            pass