# Ramanujan's Pi Estimation (7-3)

import math

acc_threshold=10e-15
k=0
const=2*math.sqrt(2)/9801

def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)

def estimate_pi():
  inv_pi=const
  while float(math.pi-inv_pi)>acc_threshold:
    inv_pi=
  