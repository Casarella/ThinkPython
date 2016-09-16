# 6-5 Greatest Common Divisor
# GCD of a and b is the largest number that divides both of them with no remainder:


def gcd(a,b):
  if b==0:
    return a
  r=a%b
  return gcd(b,r)
    
print(gcd(3,9))