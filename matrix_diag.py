# On matrix
from numpy import *

m = matrix('1 2 3; 4 5 6; 7,8,9')

for i in range(3):
    for j in range(3):
        print(m[i,j], end=' ')
    print()

print('The diagonal numbers are: ')
for i1 in range(3):
    for j1 in range(3):
        if i1 == j1:
            print(m[i1,j1], end=' ')
