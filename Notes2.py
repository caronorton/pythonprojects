import random


# Dictionary
# A dictionary is similar in a way to how we think of a switch, if we
#   limited our thinking of a switch to solely data

dictionExample = {
    "A": "You got an A",
    "B": "You got an B",
    "C": "You got an C"
}

print( dictionExample )
print( dictionExample["B"] )

# This doesn't work
# print( dictionExample["D"] )


# Note, this isn't enough for us to solve fully lab 2
# So lets add some additional functionality to the dictionary
# instead of the dictionary returning a simple String, what if it returned
# something calculated at the time?
# Note: If you use a variable in a dictionary, make sure the variable is defined
#       Before the dictionary is used.



dictionExample = {
    "A": random.randint( 90 , 100 ),
    "B": random.randint( 80 , 89 ),
    "C": random.randint( 70 , 79 )
}

print( dictionExample )
print( dictionExample["A"] )

print( dictionExample["A"] )

if "D" in dictionExample :
    print( dictionExample["D"] )
else:
    print("error")


grade = random.randint( 90 , 100 );
dictionExample = {
    "A": grade,
    "B": grade-10,
    "C": grade-20
}
print( dictionExample["A"] )
print( dictionExample["B"] )
print( dictionExample["C"] )