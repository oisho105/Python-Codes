
b = int(input('base of pyramid: '))
h = int(input('height of pyramid: '))
if h!=b:
    print('incorrect, base equals height')

else:
    for i in range(h):
        for b in range(h-i):
            print ('# ',end='')
        print ()

# print ('bye')
