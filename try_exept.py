
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))

try:          # this's a block, 'try' block
    print('resource open')
    print (a/b)

except ZeroDivisionError as e:  # 'as e', represents exception type
    print('you can\'t do ',e)

try:
    k = int(input('enter a number: '))
    print(k)

except ValueError as e:     # value error
    print('invalid input')  # if k isn't int, it'll be error

except Exception as e:      # all kinda error
    print('Something wrong')

finally:
    print('resource closed')
