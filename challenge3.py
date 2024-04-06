# palindrome

# string reversed is same as forward

original_string = "firetruck"

reversed_string = ""

for character in original_string: # f, i, r, e ....
    reversed_string = character + reversed_string # f, if, rif, erif ...

print(reversed_string)

if (reversed_string == original_string):
    print("A palindrome")
else:
    print("Not a palindrome")

# Ternary
# print("A palindrome") if reversed_string == original_string else print("Not a Palindrome")

#python can reverse string
# name[::-1] - :: means go from 'first to last' therefore ::-1 = last to first