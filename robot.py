import pygame as pg
import numpy as np
import ultil

class Robot:
    def __init__(self, x, y, diameter, color, speed):
        self.x = x
        self.y = y
        self.radius = diameter/2
        self.possesion = False
        self.color = color
        self.rect = pg.Rect(x-diameter/2, y-diameter/2, diameter, diameter)
        self.speed = speed
        self.rotation = 0

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
    
    # def grapse_ball(Self, ball):
    #     if self.hand.rect.colliderect(ball.rect) and not ball.attached:
    #         ball.attached = True
    #         ball.master = self  # Optionally link the ball to the robot
    #         print("Ball grasped by the robot.")
            
    # def update_ball_position(self, ball):
    #     if ball.attached:
    #         ball.x = self.hand.x
    #         ball.y = self.hand.y
    #         ball.update_rect()
    
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
        s_pos = ultil.find_rotation(self.x, self.y, self.radius, self.rotation)
        e_pos = ultil.find_rotation(self.x, self.y, self.radius+30, self.rotation)
        pg.draw.line(win, self.color, s_pos, e_pos, 5)

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.rect = pg.Rect(x-radius, y-radius, radius*2, radius*2)
        self.momentum = 0
        self.direction = (0, 0)
        self.attached = False
        self.master = None

    def update_rect(self):
        self.rect = pg.Rect(self.x -  self.radius, self.y - self.radius, self.radius*2, self.radius*2)
         
    def move(self):
        if not self.attached:
            self.x += self.direction[0] * self.momentum
            self.y += self.direction[1] * self.momentum
            self.update_rect()
        else:
            self.x, self.y = ultil.find_rotation(self.attached.x, self.attached.y, self.attached.radius+30, self.attached.rotation)
            self.update_rect()