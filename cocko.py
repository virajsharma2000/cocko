# importing important libary
import random
import pyfiglet
import pywhatkit
import sys

# init variable called k for asking file input in console argument
k = sys.argv[1]
# init variable called string asking input for string
string = input('string: ')
# init file name
file = open(k,'r')
# reading file in propper string
x = file.read().strip().split()

for y in x:

 # writing if for the code example if this code do this feature
 if 'capital(string)' in y:
  # building feature called capital
  string = string.capitalize()

 if 'lower(string)' in y:
  # building capital to lower converter
  string = string.lower()

 if 'replace(string)' in y:
  newstring = input('Enter new thing to written: ')
  string = newstring

 if 'remove(string)' in y:
  string = ''

 if 'length(string)' in y:
  # building string length finder
  print(int(len(string)))

 if 'show(string)' in y:
  # building string reader
  print(string)

 if 'stringtoarray()' in y:
  # building string to array converter
  print(string.split())

if 'shuffle(letters)' in y:
 # init variable of list called array
 array = []
 #init empty string
 emptystring = ''
 # creating for loop for appending each letter of string in variable called array
 for y in string:
  array.append(y)
 # jumbling array
 random.shuffle(array)
 # converting array to string
 for a in array:
  emptystring += a
 # printing the string
 string = emptystrings

 if 'check_big_string_and_small_string()' in y:
  # init variable called length finding length in variable
  length = int(len(string))
  # creating small of big checker using if and else
  if length > 5:
   print('big string')
  else:
   print('small string')
   
 if 'sort(string)' in y:
  # init variable called array2 it is array variable
  array2 = []
  # init empty string
  string2 = ''
  # creating loop for appending all the string in array2 variable
  for s in string:
   array2.append(s)
   # sorting the list
   array2.sort()
  # converting back array to string
 for so in array2:
  string2 += so

 string = string2

 if 'reverse(string)' in y:
   # init variable called reversed_string
   reversedstring = string[::-1]
   string = reversedstring
 
 if 'normal(string)' in y:
  # init normal variable for converting back string to normal string 
  normal = string[::1]
  string = normal
 
 if 'detectchars()' in y:
  # init the input variable called char
  char = input('one char: ')
  # checking if char is there inn string ot not with support of if and else
  if char in string:
   print('charecter ' + char + ' is in string')
  else:
    print('charecter ' + char + ' is not in string')

 if  'detectvovle()' in y:
  # checking vovle in string with support of if and else
  if 'a' in string or 'e' in string or 'i' in string or 'o' in string or 'u' in string:
     print('there is a vovle in string')
  else:
     print('no vovle in string')

 if 'range(string)' in y:
  # creating for loop for ranging the string
  for rangestr in string:
   print(rangestr)
 
 if 'assci(string)' in x:
  # creating feature called make assci(string)
  string = ''.join(str(ord(chars)) for chars in string)

 if 'pickanyletter(string)' in x:
  # init array variable called emptyarray
  emptyarray = []
  # creating for loop for appending
  for letters in string:
   emptyarray.append(letters)
  # chossing any letter randomly
  randomchoice = random.choice(emptyarray)
  # showing the choosed letter
  string = randomchoice

 if 'statistic(string)' in x:
  # init array variable called emptyarray2
  emptyarray2 = []
  # creating the loop for appending all string things to array
  for letter in string:
   emptyarray2.append(letter)
  # creating the statistic important thing
   print(letter,emptyarray2.count(letter))

 if 'figlet(string)' in x:
  # building asci art generator
  print(pyfiglet.figlet_format(string))

 if  'searchstring()' in x:
  # building string info search engine
  print(pywhatkit.info(string))
 
 if 'strangestring()' in x:
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
 string = c
 
 if 'searchcharindex(string)' in y:
  # init the variable called charecter
  charecter = input('charecter: ')
  # init the variable of list aclled list2
  list2 = []
  # creating for loop for appending all the thing of string to array
  for stri in string:
     list2.append(stri)
  # printing the index of the string charr
  print('index of charecter called ' + charecter + ' is',list2.index(charecter))
  
 if 'isnumeric(string)' in y:
  # building the finder of that is string have a number
  print(string.isnumeric())

 if 'islower(string)' in y:
  # building the finder of that string is lower
  print(string.islower())

 if 'removenumbers(string)' in y:
  # building number remover
  # building a empty list variable
  stringout = []
  # init empty string
  emptystring = ''
  # printing the numbers
  for strng in string:
   if not strng.isdigit():
    # appending the string things in the stringout list
    stringout.append(strng)
  # converting stringout list to back string
  for stringou in stringout:
   emptystring += stringout

 string = emptystring

 if 'createfunnysentence(likepumpu)' in y:
    # creating feature called createfunnysentencelikepumpu
    # spliting words into a list
    list = string.split()
    # shuffling the list
    random.shuffle(list)
    # init empty string
    finalres = ''
    # converting list back to string
    for x in list:
        finalres += (x + " ")
    # printing finalres variable
    string = finalres

 if 'printtype(string)' in y:
    # creating the feature called printtype(string) for printing that string is converted to integer
    print(type(string))

