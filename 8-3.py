# 8-3 is_palindrome with string slicing
# challenge mode: 1 line.

input_string=str(input('Is this word a palindrome? \n',))

def is_palindrome():
  if input_string[::-1]==input_string:
    return print('Nice. You got yourself a nice palindrome, bud.')
  else:
    return print('Nah dude.')
is_palindrome()