# 5-5.py Baby's First Fractal
# Using turtle to draw

import turtle as t

def draw(t,length,n):
  """
  Uses Turtle to draw an n-dimensional fractal with base 'length', turning an angle upwards each time by 'angle'
  """
  if n==0:
    return
  angle=50
  t.fd(length*n)
  t.lt(angle)
  draw(t,length,n-1)
  t.rt(2*angle)
  draw(t,length,n-1)
  t.lt(angle)
  t.bk(length*n)
  
draw(t,10,4)