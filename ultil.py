import math
import numpy as np

def find_rotation(x, y, r, degree):
  radian = (degree/180)*math.pi
  return x+ r*math.cos(radian), y + r*math.sin(radian)

def find_vector_rotation(vector):
  x, y = vector
  angle_rad = np.arctan2(y, x)
  angle_deg = np.degrees(angle_rad)
  return angle_deg

