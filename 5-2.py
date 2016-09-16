#5-2 Fermat's Last Theorem
# a^n+b^n=c^n does not exist for any n>2

def check_fermat(a,b,c,n):
  if n>2 and a**n+b**n==c**n:
    print('Holy smokes, Fermat was wrong!')
  else:
    print("No, that doesn't work.")

def input_prompt():
  """
  Asks the user for a,b,c,n inputs to Fermat's Last Theorem and adds the test to __main__
  """
  a=int(input('What is a?'))
  b=int(input('What is b?'))
  c=int(input('What is c?'))
  n=int(input('What is n?'))
  return check_fermat(a,b,c,n)

input_prompt()