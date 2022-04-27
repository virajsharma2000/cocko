import random
string = input('string: ')
k = input('file: ')
file = open(k,'r')
x = file.read().strip()
if x == 'capital(string)':
 print(string.capitalize())
if x == 'lower(string)':
 print(string.lower())
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
if x == 'replace(string)':
 y = input('new string: ')
 print(string.replace(string,y))
if x == 'remove(string)':
 print(string.replace(string,''))
if x == 'check_big_string_and_small_string()':
 length = int(len(string))
 if length > 5:
  print('big string')
 else:
  print('small string')
if x == 'sort(string)':
 array2 = []
 string2 = ''
 for s in string:
  array2.append(s)
 array2.sort()
 for so in array2:
  string2 += so
 print(string2)
if x == 'reverse(string)':
 reversed_string = string[::-1]
 print(reversed_string)
if x == 'normal(string)':
 normal = string[::1]
 print(normal)
if x == 'detectchars()':
 char = input('one char: ')
 if char in string:
   print('charecter ' + char + ' is in string')
 else:
    print('charecter ' + char + ' is not in string')
if x == 'detectvovle()':
 if 'a' in string or 'e' in string or 'i' in string or 'o' in string or 'u' in string:
     print('there is a vovle in string')
 else:
  print('no vovle in string')
if x == 'range(string)':
 for rangestr in string:
   print(rangestr)
if x == 'stringtoint()':
 convert = int(string)
 print('before it was: ')
 print(type(string))
 print('now it is: ')
 print(type(convert))
if x == 'stringtofloat()':
 convert2 = float(string)
 print('before it was: ')
 print(type(string))
 print('now it is: ')
 print(type(convert2))


 


