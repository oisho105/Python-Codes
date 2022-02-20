
def count(lst):
    even = 0; odd = 0
    for i in lst:
        if i%2==0:
            even +=1
        else:
            odd +=1
    return even, odd

lst = [20,30,40,65,87]
even, odd = count(lst)

print('Even: {} and Odd: {}'.format(even,odd))
    # format() is a function qualifying string
