import random


# While Loops
# First note: Do while loops do not exist in python
#             You can create the same functionality by using a true statement
#             in your while loop, and use an if to break out

# Beyond that, while loops are pretty much identical in python

x = 5
while x >= 1:
    print( x )
    x -= 1
print("The loop is over, and x is now" , x )




# For Loops
# For loops are significantly different in python
# To traverse a set of numbers, you use the range function
# Collections --> traverse using that for each style

# Range function
# range( a ) generate a series of numbers from 0 to a, going up by 1 (exclusive of a)
# range( a , b )  generate a series of numbers from a to b, going up by 1 (exclusive of b)
# range( a , b , c ) generate a series of numbers from a to b, going up by c  (exclusive of b)

for x in range( 5 ):
    print( x )
print("loop is done, what is x?",x)


for x in range( 10 , 15 ):
    print( x )
print("loop is done, what is x?",x)


# Note, you can't do reverse in the way I am trying below
for x in range( 15 , 10 ):
    print( x )
print("loop is done, what is x?",x)


for x in range( 1, 10 , 3 ):
    print( x )
print("loop is done, what is x?",x)




# to do reverse, there are two ways
for x in range( 10, 1 , -3 ):
    print( x )
print("loop is done, what is x?",x)


# Second way is just write it normal, but use the reversed function
# Note: B is still not inclusive, so becaseful where it starts
# Note: reversed also works on strings
for x in reversed( range( 1, 10 , 3 ) ):
    print( x )
print("loop is done, what is x?",x)