# fibonacci series
x = int(input('put a number: '))

def fib(n):
    a = 0;     b = 1
    if n<=0:
        print('That cant be negative')
    elif n ==1:
        print(a)
    else:
        print(a, end=' '); print(b, end=' ')
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c, end=' ')
fib(x)
