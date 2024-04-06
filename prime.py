# If a number is prime or not
number = int(input("Enter a number: ")) # eg number = 10

for i in range( 2, number): # will loop 2 - 9 searching if it is divisble from itself or 1 and no other
    if (number % i == 0):
        print("Not a prime")
        break
else:
    print("Is a prime")
    