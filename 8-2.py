#8-2 Looping and Counting a's in 'banana'

input_string=str(input('Input a word: \n',))
input_letter=str(input('Count which letter? \n',))

def in_word():
  return input_string.count(input_letter)

print(in_word())