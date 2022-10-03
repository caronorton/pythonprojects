import numpy as np

arr = np.random.randint(1, 21, size=10)
print(arr)
arrSum = 0
for x in arr:
    arrSum += x
print("The mean is", arrSum / len(arr))

small = arr[0]
index = 0
for y in arr:
    if small > y: #if the number that is being tested is smaller then the
        #current smallest set it as the smallest
        small = y
print("Your smallest number is", small)
print("The smallest number is at index", arr[small])



num1 = int(input("Enter in a number:"))
arr = []
while num1 > 0:
    d = num1 % 10
    num1 = int(num1/10)
    arr.append(d)
arr.reverse()
print("Your array is:", arr)


import numpy as np

arr1 = np.random.randint(1, 21, size=10)
arr2 = np.random.randint(1, 21, size=10)

arr1.sort()
arr2.sort()

print("int a[] =", arr1)
print("int b[] =", arr2)

arr3 = [0] * 20
x = 0
i = 0
k = 0
while x < len(arr1) and i < len(arr2):
    if arr1[x] < arr2[i]: # if one index is less then the other, add the smallest number to the combined array
        arr3[k] = arr1[x]
        x += 1
        k += 1
    else:
        arr3[k] = arr2[i]
        i += 1
        k += 1
if x == len(arr1): # if the first array is fully added, add the rest of the other
    while i < len(arr2):
        arr3[k] = arr2[i]
        i += 1
        k += 1
else:
    while x < len(arr1):
        arr3[k] = arr1[x]
        x += 1
        k += 1

print("combined array=", arr3)
