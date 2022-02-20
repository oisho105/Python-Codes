pos = 0

def search(list, n):
    i = 0
    while i< len(list):
        if list[i] == n:
            globals()['pos'] = i+1 # pos' of n
            return True
        i += 1
    return False

list = [5,8,4,6,9,2]
n = 3

if search(list,n):
    print('found at', pos)
else:
    print('not found')

# Linear search with for loop
"""
pos = 0

def search(list, n):
    e = 1
    for i in list:
        if i == n:
            globals()['pos'] = e # pos' of n
            return True
        e += 1
    return False

list = [5,8,4,6,9,2]
n = 4

if search(list,n):
    print('found at', pos)
else:
    print('not found')
"""