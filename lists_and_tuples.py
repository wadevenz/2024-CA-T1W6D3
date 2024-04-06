# Non-primitive data types - hold/store multiple pieces of data

# List - (Array in ohter languages) - collection of data - indexed - mutable (can be changed)
numbers = [13, 2, 5, 98, 56]
#           0  1  2  3   4

print(numbers)
print(numbers[2])

numbers[2] = 10
print(numbers)

numbers.append(42) # added to end of the list
print(numbers)

numbers.insert(2, 16) # inserts a new number at index "2", the rest of the list is pushed further place
print(numbers)

numbers.pop() # removes data from end of the list
print(numbers)

numbers.remove(98) # removes specific data from list
print(numbers)

numbers.sort() # default assorts in ascending order
print(numbers)

numbers.reverse() # self explanatory
print(numbers)

print(len(numbers))

# There are more functions incl "index, count"

print("\n\n\n") # \n = enter

# Tuples - collection of data - indexed - immutable

# () - small brackets - parentheses
# {} - curly brackets
# [] - big brackets - square brackets

names = ( "John", "Jane", "Mike", "Jane" ) 
# index     0       1       2       3

print (names)
print(names[1])
# names[2] = "Steve" # error due to being a tuple
# no function that changes items will work

print(len(names))
print(names.count("Jane")) # counts the number of times a data item is repeated, works as it doesnt change internal data of tuple

days_of_the_week = ( "Monday", "Tuesday", "Wednesday", "...") # example of a list you wouldnt want to change
