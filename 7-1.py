#7-1 My Square Root
import math
acc_threshold=10**-9
def mysqrt(x,a):
  y=0
  """
  Should return y=sqrt(a) algorithmically, using an initial guess x
  """
  while abs(y-x)<acc_threshold:
    print(x)
    y=(x+a/x)/2
    y=x

def test_square_root(x,a):
  print('{:<3}\t{:<12}\t{:<12}\t{}'.format('a','mysqrt(a)','math.sqrt(a)','diff'))
  print('{:<3}\t{:<12}\t{:<12}\t{}'.format('-','-','-','-'))
  print('{:<3}\t{:<12}\t{:<12}\t{}'.format(a,mysqrt(x,a),math.sqrt(a),abs(math.sqrt(a)-mysqrt(x,a))))
    
print(mysqrt(3,4))
#test_square_root(4,4)

