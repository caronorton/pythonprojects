import random
import numpy as np

# as np is an alias, which is just an alternate name referencing the import

# Functions and Scope
# First --> Don't drop all the good programming habits you have from java
#           So don't use globals when instead you should be passing parameters
# You should keep your functions seperate from other code

"""
Don't do this....

Code
code

function

code
code
"""

"""
Do this instead

function
function

code
code

"""


def exampleFunction(a, b):
    return a + b


def arrayMod(a):
    a[0] = 10


c = exampleFunction(2, 3)
print(c)

d = [3, 5, 8]  # note lists you surround with [ ] not { }
print(d)
arrayMod(d)
print(d)

"""
Note: The tutorial you did is likely the one using Lists as Arrays
If you want to learn how to use real arrays, go here
https://www.w3schools.com/python/numpy/numpy_intro.asp


Whats the difference between an Array and List?
- To use an Array, you must import NumPy package
- Arrays can only store the same data type
- Arrays need to be declared
- Arrays are great for storing data more efficiently
- Arrays are great for numerical operations
    Such as I can divide the whole array by a number with a single operation
- Much faster to use than Lists



Lists - effectively you can think of them as ArrayLists from Java
- This is what Python uses traditionally  
- Lists don't need to be declared (Arrays do)
- Great to use if you have a short set of data, and don't use mathematical operations



Tuples - we wont use, but what are they?
- They are a collection which is unchangeable once created
- Indicate tubles by using ( ) instead of [ ]


"""
# Lists
arr = []
for i in range(10):
    arr.append(random.randint(1, 10))
print(arr)

# accessing individual data is the same, with the exception of
# negative indexing
# -1   --> access last data
# -2   --> access second to last data

print(arr[0])
print(arr[-2])

# you can access group of data using ranges
print(arr[2:4])  # 2 - 3
print(arr[2:])  # 2 - end
print(arr[:4])  # start - 3

# looping over lists is like for each

for element in arr:
    print(element)

# to access indexes
for i in range(len(arr)):
    print("index=", i, "element=", arr[i])

# Numpy Arrays

arrayA = np.array([1, 2, 5, 9, 12, -4, 7])
# arrayB = numpy.arrays([4 , 3 , 5 , 7 , 1 , -3 , 0])

print("arrayA =", arrayA)

a = np.array(42)  # 0-D array, aka scalars
b = np.array([[1, 2, 3], [4, 5, 6]])
# you can even do 3D arrays, but I won't show that here

print(b.ndim)  # ndim gives the number of dimensions
print(b)

# access the index is what you would expect
print(arrayA[3])

# you can access group of data using ranges
print(arrayA[2:4])  # 2 - 3
print(arrayA[2:])  # 2 - end
print(arrayA[:4])  # start to 3

# You can even change the shape of an array
# Join arrays, split them, sort them.....