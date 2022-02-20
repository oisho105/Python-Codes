from functools import reduce

def is_even(n):
    return n%2==0   # returns true/false

nums = [2,6,8,10,11]

evens = list(filter(is_even, nums))
    # filter() takes values from nums, put it in is_even, when renders true, assigns in evens
print(evens)

doubles = list(map(lambda n:n*2, evens))
print(doubles)

sum = reduce(lambda a,b: a+b, doubles)
print(sum)
