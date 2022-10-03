import random


# IDLE is Python's Integrated Development and Learning Environment
# Has both interactive mode and a built in text editor

# String - sequence of characters that is used as data
# String Literal - string that appears in the actual code of the program

x = 10
print("x =", x) # a space is already integrated because of the comma

y = 20.5
print("x =", x, "y =", y)

x = "Hello"     #variables can be reassigned a different type
                #potentially dangerous though
print( "x =", x)

# int, float, string

x = int( input("Please enter in a number: ")) #note: no space is automatic here
print( "x =", x)

#note casting is   type( item to be cast )

# / --> float division
# // --> int division   (floor division)

x = 3.5//1.5
print( "x =", x)
x = 3.5/1.5
print( "x =", x)
# * --> mulitplation
# ** --> exponents

print("5**2 =", (5**2))

# escape characters --> "\n" new line and "\t" horizontal tab


# I won't be taking the time to point out all the String functionality
# but please make sure you know it


# if statements, end with a colon, and () are not required

x = random.randint(1, 10)  # 1 to 10  (both are inclusive)
y = random.randint(1, 10)

# from random import randint
# randint    --> I wouldn't have to say  random.randint

print("x =", x, "y =", y )

if x > y :
    print("x is the largest")
    print("more code")
elif x == y:
    print("x and y are equal")
else:
    print("y is the largest")

# use the keywords and/or
# Python uses short circuit evaluation