
def factr(x):
    f = 1
    for i1 in range(1,x+1):
        f = f *i1
    return(f)

x = int(input('put a number: '))
res = factr(x)
print(res)
