import random
import sys
import os

print("Hello World")

#comment

'''
Multi line comment
'''

name = "Michael"
print(name)

print("\" this puts a double quote in")

print(5 % 2) # modulus shows the remainder
print(5 // 2) # floor division throws out the remainder

print("%s" % (name))
print("This is how to make a new line empty line\n")
print("see..")

list_of_shit = ["juice", "groceries", "example"]

#Lists start here

print(list_of_shit[0])
list_of_shit[0] = "green juice"
print(list_of_shit[0])
print(list_of_shit[0:2]) #up to not including

more_lists = ["car","house", "shit", "dog"]

big_list = [list_of_shit, more_lists]
print(big_list)
print(big_list[1][1])

list_of_shit.append("shit")
print(list_of_shit)

list_of_shit.insert(1, "grape")
print(list_of_shit)

list_of_shit.sort()
print(list_of_shit)

list_of_shit.reverse()
print(list_of_shit)

del list_of_shit[1]
print(list_of_shit)

biggest_list = list_of_shit + more_lists
print(biggest_list)
print(len(biggest_list))
print(max(biggest_list))
print(min(biggest_list))

#Tuples start here (uneditable lists)

pi_tuple = (3,1,4,5,9,2,6,5,3,5,8,9,7,9)

turn_to_list = list(pi_tuple)
turn_back_to_tuple = tuple(turn_to_list)

print(len(pi_tuple))
print(min(pi_tuple))
print(max(pi_tuple))

#Dictionaries start here

example_dictionary = {"this is a key" : "This is a value", "key" : "value", "I love" : "Shannon"}

print(example_dictionary["key"])

del example_dictionary["this is a key"]
print(example_dictionary)

example_dictionary["I love"] = 	"Shannon a whole bunch"
print(example_dictionary)

print(len(example_dictionary))

print(example_dictionary.get("I love"))

print(example_dictionary.keys())
print(example_dictionary.values())










