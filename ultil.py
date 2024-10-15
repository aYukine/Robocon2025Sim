import math

def find_rotation(x, y, r, degree):
  radian = (degree/180)*math.pi
  return x+ r*math.cos(radian), y + r*math.sin(radian)
