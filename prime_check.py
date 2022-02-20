# prime check

num = int(input('put a number: '))

for i in range (2, num):
    if num %i == 0:
        print ('not prime')
        break       # breaks loop, so doesn't print others
else:
    print('prime')
    
