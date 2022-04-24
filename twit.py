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
