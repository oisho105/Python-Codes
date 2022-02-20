# calling from module

import math

x = math.sqrt (25)
print (x)

from math import sqrt, pow    # importing sqrt function from 'math' module
x = sqrt(25)                # now no needa put 'math'.sqrt

print(x)