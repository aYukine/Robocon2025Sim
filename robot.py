import pygame as pg

class Robot:
    def __init__(self, x, y, diameter, color):
        self.x = x
        self.y = y
        self.radius = diameter/2
        self.possesion = False
        self.color = color
        self.rect = pg.Rect(x-diameter/2, y-diameter/2, diameter, diameter)

    def update_rect(self):
        self.rect = pg.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)

    def move(self, x, y):
        self.x += x
        self.y += y
        
    def draw_robot(self, win):
        pg.draw.circle(win, self.color, (self.x, self.y), self.radius)