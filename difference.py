# difference of primitive and non-primitive data types



# PRIMITIVE
num1 = 5 # assign 5 to num1

num2 = num1 # assing the value of num1 to num2 -- copies the data by value

num1 = 10 # changed the value of num1 to 10

print(num1)
print(num2) # assignment was done prior to change of num1 -- will stay at 5

# NON-PRIMITIVE

list1 = [ 1, 2, 3, 4 ] # assign [] to list1

list2 = list1 # assign list1 to list2 -- copies by reference or copy by address aka (list1)

list1.append(5) # change something in list1

print(list1)
print(list2) # will take on list append
