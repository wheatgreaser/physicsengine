import time
import math

constants = [
  ["G", (6.67 * pow(10,-11))]
]

class Particle:
  def __init__(self, mass, position):
    self.mass = mass
    self.position = position

p1 = Particle(200, [4, 5, 0])
p2 = Particle(200, [5, 0, 3])

def distance(p1, p2):
  l = pow((p1.position[0] - p2.position[0]), 2)
  b = pow((p1.position[1] - p2.position[1]), 2)
  h = pow((p1.position[2] - p2.position[2]), 2)
  return math.sqrt(l + b + h)

def gravitational_force(p1, p2):
  F=[0, 0, 0]
  F[0] = ((constants[0][1]* p1.mass * p2.mass* (p1.position[0] - p2.position[0])))/ pow(distance(p1, p2) , 3)
  F[1] = ((constants[0][1]* p1.mass * p2.mass*(p1.position[1] - p2.position[1])))/ pow(distance(p1, p2), 3)
  F[2] = ((constants[0][1]* p1.mass * p2.mass *(p1.position[2] - p2.position[2])))/ pow(distance(p1, p2), 3)

  
  
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
def simul_gravity(duration):
  
  for i in range(duration):
    F = gravitational_force(p1, p2)
    a1 = -F[0]/p1.mass
    a2 = F[0]/p2.mass

    a3 = -F[1]/p1.mass
    a4 = F[1]/p2.mass

    a5 = -F[2]/p1.mass
    a6 = F[2]/p2.mass
  
  
    v1[0] += a1 * 1
    v2[0] += a2 * 1

    v1[1] += a3 * 1
    v2[1] += a4 * 1

    v1[2] += a5 * 1
    v2[2] += a6 * 1
   
    posUpdate(v1, p1,  1)
    posUpdate(v2, p2, 1)
    print(
  f'X1 : {p1.position[0]}, Y1 : {p1.position[1]}, Z1 : {p1.position[2]} ')
    print(
      f'X2 : {p2.position[0]}, Y2 : {p2.position[1]}, Z2 : {p2.position[2]} ')
    print(f'distance: {distance(p1, p2)}')
    print()
    time.sleep(1)


simul_gravity(20)
  
  
  
    