from numpy import *

arr1 = array([2,6,8,10,12])
# arr2 = arr1.view()  # assign values of 'arr1' to 'arr2' mirroring the address
arr2 = arr1.copy()  # assign values of arr1 to arr2 w/o mirroring

arr1[1] = 7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
