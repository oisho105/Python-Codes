# Find numbers from a list which are divisible by 5

nums = [11, 14, 18, 23, 26, 32]

for num in nums:
    if num %5 == 0:
        print (num, end=' ')
else:
    print('not found')

