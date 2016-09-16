# recurse(s,n)
# Will exhibit recursive definitions, baby loops

def recurse(s,n):
  if n==0:
    print(s)
  else:
    recurse(n-1,s+1)
    
recurse(-1,0)