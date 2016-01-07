__author__ = 'Mj'
def sum_digits(n, p):
    s = 0
    while n:
        s += int(n % p)
        n = int(n/p)
    return int(s)
n = int(input())
for i in range(11, 10**3):
    j = 2
    num = sum_digits(i, n)
    while((num**j) <= i):
        if(i == (num**j)):
            print(i, end=' ')
        j += 1