# Search in an array;
from array import *

arr = array('i',[])
n = int(input('Enter the length of the Array: '))

for i in range(n):      # user defined values put in 'arr'
    x = int(input('Enter the next value: '))
    arr.append(x)   # appends value of x to 'arr'

print('The values are: ', end='')
for i in range(n):
    print(arr[i], end=' ')
print ()           # prints a new line here

val = int(input('Enter the value for search: '))

k = 1
for e in arr:
    if e == val:
        print('index of the value is:', k)
        break
    k += 1
else:
    print('No such value was found')
    
