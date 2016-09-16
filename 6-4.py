# is_power
# Should check to see if 'a' is a power of 'b'

def is_power(a,b):
  mod=a%b
  r=a/b
  if mod!=0:
    return False
  elif r**-b%1==0:
    return True
  else:
    return is_power(r,b)
  
print(is_power(16,3))