#5-3 if_triangle definition
# Check to see if a user-input of 3 lengths could make a triangle.

def is_triangle(a,b,c):
  if (a+b>c) or (a+c>b) or (b+c>a):
    print("No.")
  elif a+b==c or a+c==b or b+c==a:
    print("Degenerate. (Yes.)")
  else:
    print("Yes.")
    
def user_inputs():
  a=int(input("Input length for a:"))
  b=int(input("Input length for b:"))
  c=int(input("Input length for c:"))
  return is_triangle(a,b,c)

user_inputs()