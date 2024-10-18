import numpy as np
import ultil
from settings import *


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
         
    def move(self, dt):
        if not self.attached:
            if self.momentum > 0:
                self.x += (self.direction[0] * self.momentum * dt)
                self.y += (self.direction[1] * self.momentum * dt)
                self.momentum -= dt*10 # decreasing factor
                if math.sqrt((self.x - 1400)**2+ (self.y - 400)**2) < 10:
                    self.x = 1395
                    self.y = 400
                    self.momentum = 0
            elif self.momentum < 0:
                self.momentum = 0
            self.update_rect()
        else:
            self.x, self.y = ultil.find_rotation(self.attached.x, self.attached.y, self.attached.radius+self.attached.hand_length, self.attached.rotation)
            self.update_rect()

class Robot:
    def __init__(self, x, y, diameter, color, speed, hand_length, hand_width, rotation):
        self.x = x
        self.y = y
        self.radius = diameter/2
        self.possesion = False
        self.hand_length = hand_length
        self.hand_width = hand_width
        self.color = color
        self.rect = pg.Rect(x-diameter/2, y-diameter/2, diameter, diameter)
        self.speed = speed
        self.rotation = rotation
        self.__dribbled = False

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
    
    def dribble(self, ball:Ball, dt):
        if not self.__dribbled:
            if ball.radius > 17:
                ball.radius -= ((dt  * 7)/dribble_time)
            elif ball.radius <= 17:
                self.__dribbled = True

        elif self.__dribbled:
            if ball.radius < 24:
                ball.radius += ((dt  * 7)/dribble_time)
            elif ball.radius >= 24:
                ball.radius = 24
                self.__dribbled = False
                return True

        print(ball.radius)
        return False
    
    def passing(self):
        pass

    def shoot(self, ball:Ball, hoop:tuple, dt):
        d_vect = (hoop[0] - self.x, hoop[1] - self.y)
        shoot_d = ultil.find_vector_rotation(d_vect)
        perform_shoot = False
        if abs(self.rotation - shoot_d - 180) < dt*rotation_speed:
            self.rotation = shoot_d + 180
            perform_shoot = True
        elif abs(self.rotation - shoot_d) > 180:
            self.rotation -= dt*rotation_speed
        elif abs(self.rotation - shoot_d) < 180:
            self.rotation += dt*rotation_speed
        else:
            pass   

        if perform_shoot:
            if not ball.attached:
                if self.hand_length < 30:
                    self.hand_length += dt*shoot_speed
                elif self.hand_length >= 30:
                    self.hand_length = 30
                    return True
            else:
                if self.hand_length > 5:
                    self.hand_length -= dt*shoot_speed
                elif self.hand_length <= 5:
                    self.hand_length = 5
                    ball.attached = False
                    ball.momentum = shoot_speed*4
                    d_vect_length = d_vect[0] + d_vect[1]
                    d_vect = (d_vect[0]/d_vect_length, d_vect[1]/d_vect_length)
                    ball.direction = d_vect
        
        return False

    def dunk(self):
        pass

    def wait(self, desired_time, total_time):
    
        if (desired_time - total_time) > 0:
            return False
        else:
            return True

    def draw_robot(self, win):
        pg.draw.circle(win, self.color, (self.x, self.y), self.radius)
        s_pos = ultil.find_rotation(self.x, self.y, self.radius, self.rotation)
        e_pos = ultil.find_rotation(self.x, self.y, self.radius+self.hand_length, self.rotation)
        pg.draw.line(win, self.color, s_pos, e_pos, self.hand_width)
