import time
import math

constants = [
  ["G", (6.67 * pow(10,-11))]
]

class Particle:
  def __init__(self, mass, position):
    self.mass = mass
    self.position = position

p1 = Particle(200000, [0, 0, 0])
p2 = Particle(200000, [5, 4, 5])

def distance(p1, p2):
  l =pow((p1[0] - p2[0]), 2)
  b = pow((p1[1] - p2[1]), 2)
  h = pow((p1[2] - p2[2]), 2)
  return math.sqrt(l + b + h)

def gravitational_force(p1, p2):
  F=[0, 0, 0]
  F[0] = (constants[0][1]* p1.mass * p2.mass )/pow(p1.position[0] - p2.position[0], 2)

  F[1] = constants[0][1]* p1.mass * p2.mass/pow(p1.position[1] - p2.position[1], 2)

  F[2] = constants[0][1]* p1.mass * p2.mass/pow(p1.position[2] - p2.position[2], 2)
  
  return F

def posUpdate(v, p, t):
  p.position[0] += v[0] * t
  p.position[1] += v[1] * t
  p.position[2] += v[2] * t
  
def posDisplay(duration, v, p) :
  for i in range(duration):
    print(f'X {p.position[0]}')
    print(f'Y {p.position[1]}')
    print(f'Z {p.position[2]}')
    print()
    posUpdate(v, p, 1)
    time.sleep(1)
    
v1 = [0, 0, 0]
v2 = [0, 0, 0]
for i in range(10):
  F = gravitational_force(p1, p2)
  a1 = F[0]/p1.mass
  a2 = F[0]/p2.mass
  v1[0] += a1 * 1
  v2[0] += a2 * 1
  posUpdate(v1, p1,  1)
  posUpdate(v2, p2, 1)
  print(f'{p1.position[0]}')
  print()
  
  
  
  
    