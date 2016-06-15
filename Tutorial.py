# import is used to make specialty functions available
# These are called modules
import random
import sys
import os

# Hello world is just one line of code
# print() outputs data to the screen
print("Hello World")

'''
This is a multi-line comment
'''

# A variable is a place to store values
# Its name is like a label for that value
name = "Derek"
print(name)

# A variable name can contain letters, numbers, or _
# but can't start with a number

# There are 5 data types Numbers, Strings, List, Tuple, Dictionary
# You can store any of them in the same variable

name = 15
print(name)

# The arithmetic operators +, -, *, /, %, **, //
# ** Exponential calculation
# // Floor Division throws out the remainder
# % Modulus Shows only the remainder
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

# Order of Operation states * and / is performed before + and -

print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

# A string is a string of characters surrounded by " or '
# If you must use a " or ' between the same quote escape it with \
quote = "\"Always remember your unique,"

# A multi-line quote
multi_line_quote = ''' just
like everyone else" '''

# String concatenation
print(quote + multi_line_quote)

# To embed a string in output use %s
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

# To keep from printing newlines use end=""
print("I don't like ", end="")
print("newlines")

# You can print a string multiple times with *
print('\n' * 5)

# LISTS -------------
# A list allows you to create a list of values and manipulate them
# Each value has an index with the first one starting at 0

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('The first item is', grocery_list[0])

# You can change the value stored in a list box
grocery_list[0] = "Green Juice"
print(grocery_list)

# You can get a subset of the list with [min:up to but not including max]

print(grocery_list[1:3])

# You can put any data type in a a list including a list
other_events = ['Wash Car', 'Pick up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]

print(to_do_list)

# Get the second item in the second list (Boxes inside of boxes)
print(to_do_list[1][1])

# You add values using append
grocery_list.append('onions')
print(to_do_list)

# Insert item at given index
grocery_list.insert(1, "Pickle")
print(grocery_list)

# Remove item from list
grocery_list.remove("Pickle")
print(grocery_list)

# Sorts items in list alphabetically or numericaly  
grocery_list.sort()
print(grocery_list)

# Reverse sort items in list
grocery_list.reverse()
print(grocery_list)

# del deletes an item at specified index
del grocery_list[4]
print(to_do_list)

# We can combine lists with a +
to_do_list = other_events + grocery_list
print(to_do_list)

# Get length of list
print(len(to_do_list))

# Get the max item in list
print(max(to_do_list))

# Get the minimum item in list
print(min(to_do_list))

# TUPLES -------------
# Values in a tuple can't change like lists

pi_tuple = (3, 1, 4, 1, 5, 9)

# Convert tuple into a list
new_tuple = list(pi_tuple)

# Convert a list into a tuple
# new_list = tuple(grocery_list)

# tuples also have len(tuple), min(tuple) and max(tuple)

# DICTIONARY or MAP -------------
# Made up of values with a unique key for each value
# Similar to lists, but you can't join dicts with a +
# {"Key" : "Value"}

super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captain Cold': 'Leonard Snart',
                  'Weather Wizard': 'Mark Mardon',
                  'Mirror Master': 'Sam Scudder',
                  'Pied Piper': 'Thomas Peterson'}

print(super_villains['Captain Cold'])

# Delete an entry
del super_villains['Fiddler']
print(super_villains)

# Replace a value
super_villains['Pied Piper'] = 'Hartley Rathaway'

# Print the number of items in the dictionary
print(len(super_villains))

# Get the value for the passed key
print(super_villains.get("Pied Piper"))

# Get a list of dictionary keys
print(super_villains.keys())

# Get a list of dictionary values
print(super_villains.values())

# CONDITIONALS -------------
# The if, else and elif statements are used to perform different
# actions based off of conditions
# Comparison Operators : ==, !=, >, <, >=, <=

# The if statement will execute code if a condition is met
# White space is used to group blocks of code in Python
# Use the same number of proceeding spaces for blocks of code

age = 30
if age > 16:
    print('You are old enough to drive')

# Use an if statement if you want to execute different code regardless
# of whether the condition ws met or not

if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

# If you want to check for multiple conditions use elif
# If the first matches it won't check other conditions that follow

if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not old enough to drive')

# You can combine conditions with logical operators
# Logical Operators : and, or, not

if (age >= 1) and (age <= 18):
    print("You get a birthday party")
elif (age == 21) or (age >= 65):
    print("You get a birthday party")
elif not (age == 30):
    print("You don't get a birthday party")
else:
    print("You get a birthday party yeah")

# FOR LOOPS -------------
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
for x in range(0, 10):
    print(x , ' ', end="")
 
print('\n')
 
# You can use for loops to cycle through a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
 
for y in grocery_list:
    print(y)
 
# You can also define a list of numbers to cycle through
for x in [2,4,6,8,10]:
    print(x)
 
# You can double up for loops to cycle through lists
num_list =[[1,2,3],[10,20,30],[100,200,300]];
 
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])
        
# WHILE LOOPS -------------
# While loops are used when you don't know ahead of time how many
# times you'll have to loop
random_num = random.randrange(0,100)
 
while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
 
# An iterator for a while loop is defined before the loop
i = 0;
while (i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue
 
    i += 1

 # USER INPUT -------------
print('What is your name?')
 
# sys.stdin.readline takes a size argurment
name = sys.stdin.readline()

# print takes a prompt arguement
name = input()
 
print('Hello', name)
 
