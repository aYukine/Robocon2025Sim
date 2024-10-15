import math

def find_rotation(x, y, r, degree):
  return x+ r*math.cos(degree), y + r*math.sin(degree)
