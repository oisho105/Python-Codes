
a = 10
b = 9
c = 11

def something():
    a = 9
    x = globals() ['a']
    print(id(x))
    print('in func:', a)
    globals() ['a']


something()
