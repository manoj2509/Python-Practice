__author__ = 'Mj'
t = int(input())
n = [[]for i in range(150)]
a = [[]for i in range(150)]
b = [[]for i in range(150)]

for i in range(t):
    n[i] = int(input())
    a[i] = int(input())
    b[i] = int(input())
for i in range(t):
    for j in range(n[i]):

        val = ((j + 1)*a[i]) + ((n[i] - j - 1)*b[i])
        print(val, end=' ')
    print()