import random
string = input('string: ')
k = input('file: ')
file = open(k,'r')
x = file.read().strip()
if x == 'capital(string)':
 print(string.capitalize())
if x == 'length(string)':
 print(int(len(string)))
if x == 'show(string)':
 print(string)
if x == 'stringtoarray()':
 print(string.split())
if x == 'shuffle(letters)':
 array = []
 emptystring = ''
 for y in string:
  array.append(y)
 random.shuffle(array)
 for a in array:
  emptystring += a
 print(emptystring)
 
