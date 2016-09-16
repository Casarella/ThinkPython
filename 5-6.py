# 5-6 Koch Curves.

import turtle as t

def koch(t,length):
  if (length%3)<1:
    t.fd(length)
    return
  red_len=length/3
  koch(t,red_len)
  t.lt(60)
  koch(t,red_len)
  t.rt(120)
  koch(t,red_len)
  t.lt(60)
  koch(t,red_len)
  
def snowflake():

  
draw(t,45,60,4)
  