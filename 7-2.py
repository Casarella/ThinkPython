# eval_loop
# Will evaluate user input until the user inputs 'done'

import math

def eval_loop():
  while True:
    eval_item=input('Input valid expression:',)
    if eval_item=='done':
      print('Thanks for playing.')
      break
    else:
      print(eval(eval_item))
      
eval_loop()
    