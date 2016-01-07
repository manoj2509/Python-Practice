__author__ = 'Mj'


def printnoloop(n, k=0):
    if(k == 0):
        n -= 5
        if n < 0:
            k = 1
        print(n, end=" ")
    else:
        n += 5
        print(n, end=" ")
    if n != orig:
        printnoloop(n, k)

n = int(input())
orig = n
print(n, end=" ")
printnoloop(n)