# Varibles and Strings
# Hello World
print("Hello world!")
# Hello World with Variable
msg = "Hello world!"
print(msg)

# Concatenation
firstName = 'beth'
lastName = 'Newton'
print (firstName + '' + lastName)

# Math
print (4 + 4)
print (4 - 4)
print (4 * 4)
print (25 ** .5)
print (100 / 10)
print (36 // 6)
print (4 % 20)

# Lists
# Make a List
bikes = ['trek', 'redline', 'giant']
# Get the First Item in a List
firstBike = bikes[0]
# Get the Last Item in a List
lastBike = bikes[-1]
# Looping Through a List for bike in bikes:
for bike in bikes:
    print(bike)
# Adding Items to a List
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')
# Making Numerical Lists
squares = []
for x in range(1, 11):
    squares.append(x**2)
# List Comprehensions
squares = [x**2 for x in range(1, 11)]
# Slcing a List
finishers = ['sam', 'bob', 'ada', 'bea']
firstTwo = finishers[:2]
# Copying a List
copyOfbikes = bikes[:]

# Lyrics
def printLyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def returnLyrics():
    lyrics = ("I'm a lumberjack, and I'm okay.")
    lyrics = lyrics + ("I sleep all night and I work all day.")
    return lyrics
lumberjackSong = returnLyrics()

printLyrics ()
print (returnLyrics())

# Some Function
def someFunction ():
    print ("This, that")
    print ("and something")
someFunction ()

# Tuples
# Making a Tuple
dimensions = (1920, 1080)

# While Statements

i = 0
while i < 5:
    print ('hello')
    i += 1

for number in range(12,20):
    print(number)
    
i = 0
j = 0
while i < 5:
    while j < 5:
        print(j, end='')
        j += 1
    print ('\n###############')
    j = 0
    i += 1

# If Statement
numb = 1
if numb == 1:
    print ("one")
elif numb == 2:
    print ("two")
else:
    print ("bigger number")
# While Using Range ()
for number in range (12, 20) :
     print (number)

# Boolean Operator
x = 41
if x == 42: # equals
    print ("equals")
if x != 42: # not equals
    print ("not equals")
if x > 42: # greater than
    print ("greater than")

# Boolean Operators Part Two
if x >= 42: # greater than or equal to
    print ("greater than or equal to")
if x < 42: # less than
    print ("less than")
if x <= 42: # less than or equal to
    print ("less than or equal to")

# Dictionaries

favFoods = {'cheese': 'camembert', 'meat': 'beef', 'vegetable': 'carrort'}
#favFood = {'cheese': 'camembert', 'meat': 'beef', 'vegetable': 'carrort'}

# As directed by pep 8 do not exceed 80 characters per line

#for foodType, type in food in favFoods.items():
for foodType, food in favFoods.items():
    print ('My favorite' + foodType + 'is:' + food)

# Dictionaries
favFoods = {'cheese': 'camembert',
            'meat': 'beef',
            'vegetable': 'carrot',
            'desert': 'pie',
            'meat product' : 'spam'
            }

fruits = ['apple', 'orange', 'peach', 'grapefruit']

# Array Slice
twoFruits=fruits[1:3]
for fruit in twoFruits:
    print(fruit)

# str.find()
# use when the index of the subString is needed
string = "catch my catatonic cat."
subString = "cat"
stringIndex = string.find(subString)
print(stringIndex)

# using the operator "in"
# "in" will return a boolean
if(subString in string):
    print("yes")
else:
    print("no")

# str.lower()
# convert a string to a lower will allow you to make
# comparisons that ignore case
crazyString = "It will be easy to cAtch my cAtAtonic cat."
stringIndex = crazyString.find(subString)
print(stringIndex)
stringIndex = crazyString.lower().find(subString)
print(stringIndex)

# str.lower() doesn't change str
# the second print statement
# prints the original crazyString
print(crazyString.lower())
print(crazyString)

# comparison operator
if crazyString > string:
    print("crazy")
else:
    print("lower is greater than upercase")
if "z" < "a":
    print("uppercase letters come first")

# str.find() [optionalm parameters]
stringIndex = string.find(subString, 19)
print(stringIndex)

# str.split()
someValues = "Laconia Gilford Belmont"
listOfValues = someValues.split()
print(listOfValues[1])

# str.split()
keyValuePairs = "Bill: Laconia, Jane: Gilford, Tom: Belmont"
listOfPairs = keyValuePairs.split(', ')
count = 0
while count < len(listOfPairs):
    fname, town = listOfPairs[count].split(": ")
    print("first name is: " + fname + "\n town is: " + town)
    count += 1

# findNeedle
def findNeedle(needle, hayStack):
    hayStack = hayStack.strip().lower()
    needle = needle.lower()
    psn = hayStack.find(needle)

    while (psn >= 0):
        before = " "
        after = " "
        if psn > 0:
            before = hayStack[psn - 1: psn]
        if psn + len(needle) < len(hayStack):
            after = hayStack[psn + len(needle): psn + len(needle) + 1]

        if (before < 'a' or before > 'z') and (after < 'a'  or after > 'z'):
            return True
        psn = hayStack.find(needle, psn + 1);
    return False

# goodbye
if count == 7:
        s = input('Would you like to chat more?\n')
        if findNeedle('yes', s):
            s = input('Great! do  you have any pets? \n')
            count = 0
        else:
            print('Good bye')

# Git -- day 1

# Set Config. Attributes
# git config --global user.name ‘BethNewton’
# git config --global user.email ‘bethnewton11.17@gmail.com’

# Naviagate to your Folder
# cd c:		will take you to the root of the c: drive
# ls -la   	will display your directory

# Create a New Repo
# git init repo

# Add a Commit
# git add <filename>
# git commit -m ‘message’

# Git -- day 2
# git add filename
# git commit -m 'message'
# git pish origin master


