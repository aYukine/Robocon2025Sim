import math
import numpy as np
import pygame

def find_rotation(x, y, r, degree):
  radian = (degree/180)*math.pi
  return x+ r*math.cos(radian), y + r*math.sin(radian)

def find_vector_rotation(vector):
  x, y = vector
  angle_rad = np.arctan2(y, x)
  angle_deg = np.degrees(angle_rad)
  return angle_deg


def write(master, color, text, x, y, pos, size):
    font = pygame.font.Font(None, size)
    if pos == "TOPLEFT":
        master.blit(font.render(str(text), True, color), (x, y))
    if pos == "MIDDLE":
        width, height = font.size(text)
        master.blit(font.render(str(text), True, color), (x-(width/2), y-(height/2)))
        