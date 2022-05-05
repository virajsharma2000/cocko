# importing important libary
import random
import pyfiglet
import pywhatkit


# init varible called string asking input for string
string = input('string: ')
# init varible called k  asking input for file
k = input('file: ')
# init file name
file = open(k,'r')
# reading fiile in propper string
x = file.read().strip()
# writing if for the code example if this code do this feature
if x == 'capital(string)':
 # building feature called capital
 print(string.capitalize())

if x == 'lower(string)':
 # building capital to lower converter
 print(string.lower())

if x == 'length(string)':
 # building string length finder
 print(int(len(string)))

if x == 'show(string)':
 # building string reader
 print(string)

if x == 'stringtoarray()':
 # building string to array converter
 print(string.split())

if x == 'shuffle(letters)':
 # init varible of list called array
 array = []
 #init empty string
 emptystring = ''
 # creating for loop for appending each letter of string in varible called array
 for y in string:
  array.append(y)
 # jumbling array
 random.shuffle(array)
 # converting array to string
 for a in array:
  emptystring += a
 # printing the string
 print(emptystring)

if x == 'replace(string)':
 # init varible called y of input
 y = input('new string: ')
 # updating the string
 print(string.replace(string,y))

if x == 'remove(string)':
 # building string remover
 print(string.replace(string,''))

if x == 'check_big_string_and_small_string()':
 # init varible called length finding length in varible
 length = int(len(string))
 # creating small of big checker using if and else
 if length > 5:
  print('big string')
 else:
  print('small string')
if x == 'sort(string)':
 # init varible called array2 it is array varible
 array2 = []
 # init empty string
 string2 = ''
 # creating loop for appending all the string in array2 varible
 for s in string:
  array2.append(s)
  # sorting the list
  array2.sort()
  # converting back array to string
 for so in array2:
  string2 += so
 print(string2)

if x == 'reverse(string)':
 # init varible called reversed_string
 reversed_string = string[::-1]
 # show the reversed string
 print(reversed_string)

if x == 'normal(string)':
 # init normal varible for converting back string to normal string 
 normal = string[::1]
 print(normal)

if x == 'detectchars()':
 # init the input varible called char
 char = input('one char: ')
 # checking if char is there inn string ot not with support of if and else
 if char in string:
   print('charecter ' + char + ' is in string')
 else:
    print('charecter ' + char + ' is not in string')

if x == 'detectvovle()':
 # checking vovle in string with support of if and else
 if 'a' in string or 'e' in string or 'i' in string or 'o' in string or 'u' in string:
     print('there is a vovle in string')
 else:
  print('no vovle in string')

if x == 'range(string)':
 # creating for loop for ranging the string
 for rangestr in string:
   print(rangestr)

if x == 'stringtoint()':
 # init intiger varible called convert converts str to int
 convert = int(string)
 # showing the that it converted the str to int
 print('before it was: ')
 print(type(string))
 print('now it is: ')
 print(type(convert))

if x == 'stringtofloat()':
 # init te float varible for converting the str to float
 convert2 = float(string)
 # showing that it converted the str to float
 print('before it was: ')
 print(type(string))
 print('now it is: ')
 print(type(convert2))

if x == 'assci(string)':
 # ranging string charecter
 for x in string:
  # convert ing the string to assci numbers
  print(ord(x))

if x == 'pickanyletter(string)':
 # init array varible called emptyarray
 emptyarray = []
 # creating for loop for appending
 for letters in string:
   emptyarray.append(letters)
 # chossing any letter randomly
 letter = random.choice(emptyarray)
 # showing the choosed letter
 print(letter)

if x == 'statistic(string)':
 # init array varible called emptyarray2
 emptyarray2 = []
 # creating the loop for appending all string things to array
 for letter in string:
  emptyarray2.append(letter)
  # creating the statistic important thing
  print(letter,emptyarray2.count(letter))

if x == 'figlet(string)':
 # building asci art generator
 print(pyfiglet.figlet_format(string))

if x == 'searchstring()':
 # building string info search engine
 pywhatkit.info(string)

if x == 'hashstring()':
 # creating hash maker
 print(str(hash(string)))

if x == 'strangestring()':
 # init the empty string
 c = ''
 # creating for loop for ranging string chars then convert them into assci number then subtarct assci number into the what letter comes before the string letter
 for s in string:
  assci = int(ord(s) - 1)
  # converting assci numbers into back string
  asscitostr = chr(assci)
  # puting all assci to str things into empty string
  c += asscitostr
  # showing the string that what strange word it written
 print(c)

if x == 'searchcharindex(string)':
 # init the variable called charecter
 charecter = input('charecter: ')
 # init the varible of list aclled list2
 list2 = []
 # creating for loop for appending all the thing of string to array
 for stri in string:
     list2.append(stri)
 # printing the index of the string charr
 print('index of charecter called ' + charecter + ' is',list2.index(charecter))
  
if x == 'isnumeric(string)':
 # building the finder of that is string have a number
 print(string.isnumeric())

if x == 'islower(string)':
 # building the finder of that string is lower
 print(string.islower())
    
