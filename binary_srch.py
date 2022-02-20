pos = 0

def search(list, n):
    l = 0
    u = len(list)-1

    while l < u:
        mid = (l+u)//2      # int' division
        if list[mid] == n:
            globals()['pos'] = mid+1
            return True

        elif u - l <= 1:
            return False    # breaks, as not found

        else:
            if list[mid] < n: l = mid
            else: u = mid   # reassigns up/low values

list = [5, 30, 55, 81, 107, 110]
n = 30

if search(list,n):
    print('found at', pos)
else:
    print('not found')
